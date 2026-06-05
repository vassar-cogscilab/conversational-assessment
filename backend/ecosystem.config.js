// pm2 process definition for the backend. The deploy workflow runs
//   pm2 startOrReload ecosystem.config.js --update-env
// from the deployed backend directory on the EC2 box.
module.exports = {
  apps: [
    {
      name: 'convo-api',
      script: 'server.js',
      cwd: '/home/ec2-user/convo-api',
      instances: 1,
      autorestart: true,
      env: {
        NODE_ENV: 'production',
        PORT: 3001,
      },
    },
  ],
};
