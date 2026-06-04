import os
from flask import Flask, Blueprint, render_template_string, jsonify, request

app = Flask(__name__)

# Trinity Rules HTML
TRINITY_RULES = """
<h2>The Holy Trinity Law</h2>
<ul>
  <li><b>1-4-7 — Vision</b>: The sovereign intention.</li>
  <li><b>2-5-8 — Structure</b>: The organizing form.</li>
  <li><b>3-6-9 — Manifestation</b>: The creative force.</li>
</ul>
<p>Everything mirrors. Everything is divisible by 3. Everything is fractal.</p>
"""

# Blueprint for core routes (3-6-9 Manifestation Layer)
core_bp = Blueprint('core', __name__)

@core_bp.route('/')
def home():
    return render_template_string(
        """
        <!doctype html>
        <html lang='en'>
          <head>
            <meta charset='utf-8'>
            <title>Holographic Trinity v15.0.0</title>
            <style>
              body {font-family: 'Inter', sans-serif; background:#0a0a0a; color:#e0e0e0; display:flex; justify-content:center; align-items:center; height:100vh; margin:0;}
              .card {background:rgba(255,255,255,0.08); padding:2rem; border-radius:12px; backdrop-filter:blur(8px); max-width:600px; text-align:center;}
              h1 {color:#fffae6;}
            </style>
          </head>
          <body>
            <div class='card'>
              <h1>Holographic Trinity v15.0.0</h1>
              {{ rules|safe }}
            </div>
          </body>
        </html>
        """,
        rules=TRINITY_RULES,
    )

# Atomic Podcast Blueprint (3-6-9 Manifestation Body)
podcast_bp = Blueprint('podcast', __name__)

@podcast_bp.route('/atomic_podcast')
def atomic_podcast():
    """A minimal placeholder for the first working manifestation.
    Returns a JSON payload describing the podcast episode.
    """
    payload = {
        "title": "Atomic Podcast – Genesis",
        "description": "The inaugural manifestation of the holographic Trinity organism.",
        "audio_url": "https://example.com/atomic_podcast.mp3",
        "trinity_layer": "3-6-9",
    }
    return jsonify(payload)

# Voice Input Placeholder Blueprint (2-5-8 Structure Layer)
voice_bp = Blueprint('voice', __name__)

@voice_bp.route('/voice_input', methods=['POST'])
def voice_input():
    """Placeholder endpoint for future voice‑to‑text integration.
    Expects a JSON body with a 'transcript' field. Returns echo.
    """
    data = request.get_json(silent=True) or {}
    transcript = data.get('transcript', '')
    return jsonify({"received": transcript, "status": "placeholder"})

# Register blueprints
app.register_blueprint(core_bp)
app.register_blueprint(podcast_bp)
app.register_blueprint(voice_bp)

if __name__ == '__main__':
    port = int(os.getenv('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
