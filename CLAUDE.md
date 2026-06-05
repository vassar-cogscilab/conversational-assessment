# CLAUDE.md

Guidance for working in this repository.

## What this is

A conversational assessment app. It will have a **web frontend** and a **simple
Node backend**. As of now only the deployment scaffolding exists — the actual app
is yet to be built. The placeholders (`frontend/public/index.html`,
`backend/server.js`) are intentionally minimal and meant to be replaced.

## Repository layout

```
frontend/public/   Static frontend (placeholder). Becomes a real build later.
backend/           Node backend run under pm2 as "convo-api" (port 3001).
deploy/            Apache reverse-proxy config installed on the server.
.github/workflows/ deploy.yml — push-to-main auto-deploy.
DEPLOY.md          Full deployment runbook (server setup, secrets, ops).
```

## Deployment — the critical constraints

The app is served under a **subpath** on a shared lab server, not at a domain
root. This shapes how the app must be built. Full details in `DEPLOY.md`; the
non-negotiables:

| URL | Served by |
| --- | --- |
| `https://cogsciresearch.vassar.edu/convo/` | Static files in `/var/www/html/convo/` (Apache, directly) |
| `https://cogsciresearch.vassar.edu/convo/api/` | Apache proxy → `http://127.0.0.1:3001` (Node + pm2) |

1. **Frontend must use base path `/convo/`.** When you add a bundler, set it
   (Vite `base: '/convo/'`, CRA `"homepage": "/convo"`, Next `basePath: '/convo'`)
   or every asset and route 404s. Build must emit to `frontend/dist`, then set
   `FRONTEND_SRC: frontend/dist` in `.github/workflows/deploy.yml` and uncomment
   its build step.
2. **All API routes live under `/convo/api/`.** The bare `/api/` route on the
   server belongs to a different app — do not use it. The backend itself sees
   prefix-stripped paths (e.g. request to `/convo/api/health` arrives as
   `/health`). Frontend should call the API via the **relative** path `api/...`.
3. **Backend listens on port 3001, bound to `127.0.0.1`.** Public traffic only
   comes through Apache. Port 3000 is taken by another app.

## How deploys happen

Push to `main` → GitHub Actions rsyncs the frontend and backend to the EC2 box
and runs `pm2 startOrReload`. No manual steps. It can also be triggered from the
Actions tab. The first deploy is already live and verified.

## Environment / runtime notes

- Server: Amazon Linux 2023, **Apache (httpd)** — not nginx. **No Docker**; the
  convention is static folders + pm2-managed Node processes. Match that style.
- Node 20 (via nvm) on the server. The backend currently has zero dependencies
  (plain `http` module). When you add deps, commit a `package-lock.json` — the
  deploy runs `npm ci --omit=dev` only if a lockfile is present.
- Secrets/env: copy `.env.example` → real `.env` (gitignored). Document any new
  env var you introduce.

## Cautions

- **It's a shared production server** hosting many other people's experiments
  under `/var/www/html`. A broken Apache config takes them all down — always
  `sudo apachectl configtest` before `sudo systemctl reload httpd`.
- TLS is Let's Encrypt with auto-renewal via a `certbot-renew.timer` systemd
  timer (cron is not installed on this box).

## Conventions

- Keep the frontend a static build deployed to the docroot; keep the backend a
  single pm2 service. Don't introduce Docker/containers — it fights the grain of
  this server.
- This is a "conversational" assessment, so the app will likely call an LLM. If
  it uses Claude, default to the latest stable models (e.g. Opus 4.8 /
  Sonnet 4.6) and keep API keys in env, never in the repo.
