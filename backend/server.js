// Minimal placeholder backend for the conversational-assessment app.
// Runs as a pm2 process ("convo-api") on the EC2 box and is reached through
// Apache at https://cogsciresearch.vassar.edu/convo/api/ -> http://127.0.0.1:3001/
//
// Apache strips the /convo/api/ prefix, so this server sees paths like "/" and
// "/health". Replace the routing below with the real backend when ready
// (swap in Express/Fastify/etc. and add a package.json with deps).

const http = require('http');

const PORT = process.env.PORT || 3001;

const server = http.createServer((req, res) => {
  res.setHeader('Content-Type', 'application/json');

  if (req.url === '/' || req.url === '/health') {
    res.writeHead(200);
    // hasApiKey lets us confirm the .env was loaded without exposing the key.
    res.end(
      JSON.stringify({
        ok: true,
        service: 'convo-api',
        hasApiKey: Boolean(process.env.ANTHROPIC_API_KEY),
      }),
    );
    return;
  }

  res.writeHead(404);
  res.end(JSON.stringify({ error: 'not found' }));
});

// Bind to localhost only — public traffic must come through Apache.
server.listen(PORT, '127.0.0.1', () => {
  console.log(`convo-api listening on http://127.0.0.1:${PORT}`);
});
