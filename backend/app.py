# Minimal placeholder backend for the conversational-assessment app.
# Runs as a pm2 process ("convo-api") on the EC2 box and is reached through
# Apache at https://cogsciresearch.vassar.edu/convo/api/ -> http://127.0.0.1:3001/
#
# Apache strips the /convo/api/ prefix, so this server sees paths like "/" and
# "/health". Replace the routing below with the real backend when ready
# (add routes here and pin new deps in requirements.txt).
#
# In production this is served by gunicorn (see ecosystem.config.js); the
# __main__ block below is only for local dev (`python app.py`).

import os

from dotenv import load_dotenv
from flask import Flask, jsonify, render_template

# Load /home/ec2-user/convo-api/.env into the environment at startup. The deploy
# writes this file from the LLM_API_KEY secret. No-op when the file is absent
# (e.g. local dev without a .env).
load_dotenv()

app = Flask(__name__)


@app.get("/")
@app.get("/health")
def health():
    # hasApiKey lets us confirm the .env was loaded without exposing the key.
    return jsonify(
        ok=True,
        service="convo-api",
        hasApiKey=bool(os.environ.get("ANTHROPIC_API_KEY")),
    )

@app.errorhandler(404)
def not_found(_err):
    return jsonify(error="not found"), 404


if __name__ == "__main__":
    # Bind to localhost only — public traffic must come through Apache.
    port = int(os.environ.get("PORT", 3001))
    app.run(host="127.0.0.1", port=port)
