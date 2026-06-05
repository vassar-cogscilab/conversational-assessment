// pm2 process definition for the backend. The deploy workflow runs
//   pm2 startOrReload ecosystem.config.js --update-env
// from the deployed backend directory on the EC2 box.
module.exports = {
  apps: [
    {
      name: 'convo-api',
      script: 'server.js',
      cwd: '/home/ec2-user/convo-api',
      // Load /home/ec2-user/convo-api/.env into process.env at startup.
      // Node >=20.12 supports --env-file-if-exists (no-op if the file is absent,
      // e.g. local dev). The deploy writes .env from the LLM_API_KEY secret.
      node_args: '--env-file-if-exists=.env',
      instances: 1,
      autorestart: true,
      env: {
        NODE_ENV: 'production',
        PORT: 3001,
      },
    },
  ],
};
