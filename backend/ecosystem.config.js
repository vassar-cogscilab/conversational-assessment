// pm2 process definition for the backend. The deploy workflow runs
//   pm2 startOrReload ecosystem.config.js --update-env
// from the deployed backend directory on the EC2 box.
//
// The backend is a Python/Flask app served by gunicorn. pm2 (running under
// Node/nvm) supervises the gunicorn process — same single-pm2-service
// convention as before, just a different runtime.
module.exports = {
  apps: [
    {
      name: 'convo-api',
      // Run gunicorn straight from the project virtualenv. The deploy creates
      // ./venv and pip-installs requirements.txt into it.
      script: './venv/bin/gunicorn',
      // interpreter "none" => exec the script directly instead of wrapping it
      // with node. gunicorn loads the Flask app object `app` from app.py and
      // binds to localhost only — public traffic must come through Apache.
      interpreter: 'none',
      // Single worker: sessions.json is a plain file written from an
      // in-memory dict, not a shared store — a second worker would keep its
      // own copy and the two would clobber each other's writes.
      args: 'app:app --bind 127.0.0.1:3001 --workers 1',
      cwd: '/home/ec2-user/convo-api',
      // Single fork process so a failed start can't hang a deploy's reload.
      exec_mode: 'fork',
      instances: 1,
      autorestart: true,
      env: {
        // app.py also load_dotenv()s the .env the deploy writes; PORT here is
        // informational (gunicorn binds via --bind above).
        PORT: 3001,
      },
    },
  ],
};
