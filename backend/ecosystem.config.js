// pm2 process definition for the backend. The deploy workflow runs
//   pm2 startOrReload ecosystem.config.js --update-env
// from the deployed backend directory on the EC2 box.
module.exports = {
  apps: [
    {
      name: 'convo-api',
      script: 'server.js',
      cwd: '/home/ec2-user/convo-api',
      // Run as a single fork process (not cluster) so a failed start can't hang
      // a deploy's graceful reload.
      exec_mode: 'fork',
      instances: 1,
      // Load /home/ec2-user/convo-api/.env into process.env at startup. The
      // deploy writes this file from the LLM_API_KEY secret. Requires Node
      // >=22.9 for --env-file-if-exists (no-op when the file is absent, e.g.
      // local dev).
      node_args: '--env-file-if-exists=.env',
      autorestart: true,
      env: {
        NODE_ENV: 'production',
        PORT: 3001,
      },
    },
  ],
};
