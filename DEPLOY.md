# Deployment

This app is deployed to the shared lab EC2 box (`cogsciresearch.vassar.edu`,
Amazon Linux 2023) and served under a subpath:

| URL | Served by |
| --- | --- |
| `https://cogsciresearch.vassar.edu/convo/` | Static files in `/var/www/html/convo/` (Apache, directly) |
| `https://cogsciresearch.vassar.edu/convo/api/` | Apache `ProxyPass` → `http://127.0.0.1:3001` (Flask/gunicorn + pm2, app `convo-api`) |

Deploys are automatic: pushing to `main` runs `.github/workflows/deploy.yml`,
which rsyncs the frontend and backend to the box and reloads pm2. It can also be
triggered manually from the Actions tab (`workflow_dispatch`).

> This is a **shared** server hosting other people's experiments under
> `/var/www/html`. The deploy only writes to `/convo` and `~/convo-api`, and the
> only Apache change is one new file. Always `apachectl configtest` before
> reloading httpd.

---

## One-time server setup

Run once on the box (`ssh -i ~/.ssh/jpsychaws.pem ec2-user@cogsciresearch.vassar.edu`).

1. **Create the deploy directories:**
   ```bash
   mkdir -p /var/www/html/convo ~/convo-api
   ```

2. **Install the Apache proxy rule:**
   ```bash
   # from a checkout of this repo on the box, or scp the file up
   sudo cp deploy/convo-proxy.conf /etc/httpd/conf.d/
   sudo apachectl configtest         # must print "Syntax OK"
   sudo systemctl reload httpd
   ```

3. **Make pm2 survive reboots** (if not already configured for this user):
   ```bash
   pm2 startup    # run the sudo command it prints
   pm2 save
   ```

> The backend runs on **Python 3 + gunicorn** inside a virtualenv
> (`~/convo-api/venv`). `python3` and the `venv` module ship with Amazon Linux
> 2023, so no extra install is needed — the deploy creates and populates the
> venv automatically. pm2 still supervises the process and runs under Node/nvm.

That's it — the GitHub Actions workflow handles the actual app deploy from then on.

## One-time GitHub setup

Add these repository secrets (Settings → Secrets and variables → Actions):

| Secret | Value |
| --- | --- |
| `EC2_HOST` | `cogsciresearch.vassar.edu` |
| `EC2_USER` | `ec2-user` |
| `EC2_SSH_KEY` | A private SSH key whose public half is in `~ec2-user/.ssh/authorized_keys` |
| `LLM_API_KEY` | Anthropic API key. The deploy writes it to `~/convo-api/.env` as `ANTHROPIC_API_KEY` (mode 600). |
| `VOYAGE_API_KEY` | Voyage AI key for RAG embeddings (`RAG_5-9/database_engine.py`). Written to the same `.env` as `VOYAGE_API_KEY`. Get one at dash.voyageai.com — free for this project's volume. |
| `ADMIN_TOKEN` | Shared secret for the `/convo/api/admin/sessions` endpoints. Written to the same `.env`. Generate with `python3 -c "import secrets; print(secrets.token_hex(32))"`. |

### Repository variables (Settings → Secrets and variables → Actions → **Variables**)

These are non-secret configuration, so they're variables rather than secrets —
being able to read the current value back in the Actions UI is the point. All
are optional; unset means the default in `backend/llm.py` applies.

| Variable | Default | Value |
| --- | --- | --- |
| `LLM_BACKEND` | `anthropic` | `anthropic` or `ollama` — which backend the examiner calls. |
| `OLLAMA_HOST` | `http://lambda-server:11434` | Ollama base URL. Plain `http://` is correct — `tailscale serve --tcp` is a raw TCP forwarder, so `https://` to this port fails. |
| `OLLAMA_MODEL` | `gemma4:26b` | Model tag to run. |
| `OLLAMA_NUM_CTX` | *(server default)* | Set to `32768` for `llama3.3:70b` — at the server's default 128K context it overflows VRAM, spills to CPU, and drops to ~2.4 tok/s. |
| `OLLAMA_KEEP_ALIVE` | `-1` | How long Ollama keeps the model resident; `-1` never unloads, so the first student after an idle stretch doesn't pay a ~17 GB cold start. |

> ⚠️ **The deploy rewrites `~/convo-api/.env` from scratch on every push.**
> Editing `.env` over SSH works until the next deploy silently reverts it — an
> `LLM_BACKEND` flipped by hand would quietly fall back to Anthropic. Change the
> repository variable and re-run the deploy instead.

**Switching the examiner to the self-hosted GPU box** requires the EC2 box to be
on the Tailscale tailnet with `lambda-server` resolvable. Both nodes were
brought up with `--accept-dns=false`, so MagicDNS names do **not** resolve; the
EC2 box has an `/etc/hosts` entry mapping `lambda-server` to its tailnet IP.
Verify before flipping the variable:

```bash
curl -s http://lambda-server:11434/v1/models | python3 -m json.tool
```

Confirm the switch took effect after the deploy — `/convo/api/health` reports
the active backend and model:

```bash
curl -s https://cogsciresearch.vassar.edu/convo/api/health
# {"ok":true,"service":"convo-api","backend":"ollama","model":"gemma4:26b",...}
```

**Recommended:** generate a dedicated deploy key rather than reusing the instance
`.pem`, so it can be rotated/revoked independently:
```bash
ssh-keygen -t ed25519 -f convo-deploy -C "github-actions convo deploy" -N ""
# append convo-deploy.pub to ~ec2-user/.ssh/authorized_keys on the box,
# paste the contents of convo-deploy (private) into the EC2_SSH_KEY secret,
# then delete the local copies.
```

---

## How a deploy works

On push to `main`, the workflow:

1. Checks out the repo.
2. (Optional, currently disabled) builds the frontend — see below.
3. `rsync`s `frontend/public/` → `/var/www/html/convo/` (`--delete`).
4. `rsync`s `backend/` → `~/convo-api/` (excludes `venv`, `__pycache__`, `.env`).
5. `rsync`s `RAG_5-9/` → `~/RAG_5-9/` — a sibling of `~/convo-api/`, mirroring
   `RAG_5-9` living alongside `backend/` in the repo.
6. SSHes in, creates the `venv` if missing, `pip install`s
   `requirements.txt` into it, then runs
   `pm2 startOrReload ecosystem.config.js` and `pm2 save`.

## Adding a real frontend (bundler)

The placeholder frontend is plain static HTML in `frontend/public/`. When you
adopt a framework:

1. Configure the **base path** to `/convo/` — this is essential or all asset and
   route URLs will 404:
   - Vite: `base: '/convo/'` in `vite.config`
   - Create React App: `"homepage": "/convo"` in `package.json`
   - Next.js: `basePath: '/convo'` in `next.config`
2. Make the build emit to `frontend/dist`.
3. In `.github/workflows/deploy.yml`: set `FRONTEND_SRC: frontend/dist` and
   uncomment the `setup-node` + build steps.
4. Call the API via the relative path `api/...` (resolves to `/convo/api/...`).

For client-side routing (SPA deep links), you'll also need an Apache rewrite so
unknown `/convo/*` paths fall back to `index.html`. Ask when you get there.

## Ops cheatsheet (on the box)

```bash
pm2 status                 # is convo-api running?
pm2 logs convo-api         # tail backend logs (gunicorn stdout/stderr)
pm2 restart convo-api      # manual restart
curl -s localhost:3001/health           # backend directly
curl -s https://cogsciresearch.vassar.edu/convo/api/health   # through Apache

# Local dev (from backend/):
python3 -m venv venv && ./venv/bin/pip install -r requirements.txt
./venv/bin/python app.py                 # Flask dev server on :3001
```
