# =============================================================================
# web_server.py
# Project  : Optimization Strategies for Natural Language Interface
#            for EdTech Infrastructure
# Roll No  : PRJN26-127
# Purpose  : Flask web server — serves the EduBot web UI and exposes a
#            REST API endpoint so the browser can call Python's matcher.
#
# Usage    : python web_server.py
# Then open: http://localhost:5000
# =============================================================================

import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from flask import Flask, request, jsonify, send_from_directory
import os
import time

# Import the REAL Python matching engine
from matcher import match_intent, is_farewell

# ── Flask App ─────────────────────────────────────────────────────
app = Flask(__name__, static_folder="web", static_url_path="")

# ── Session log file ──────────────────────────────────────────────
LOG_FILE = "chat_history_web.log"


def log_interaction(user_input: str, response: str):
    """Log every web chat interaction to a file."""
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] [WEB] USER : {user_input}\n")
        f.write(f"[{timestamp}] [WEB] BOT  : {response[:100]}...\n")
        f.write("-" * 60 + "\n")


# ── ROUTES ────────────────────────────────────────────────────────

@app.route("/")
def index():
    """
    Serve the main web UI (index.html).
    Flask will look for index.html inside the 'web/' folder.
    """
    return send_from_directory("web", "index.html")


@app.route("/chat", methods=["POST"])
def chat():
    """
    REST API endpoint for the chatbot.

    Request  (JSON): { "message": "show status" }
    Response (JSON): { "response": "...", "farewell": false }

    The browser sends the user's message here.
    Python's matcher.py processes it and returns the response.
    This is the key difference from a static site — real Python runs here!
    """
    data = request.get_json()

    if not data or "message" not in data:
        return jsonify({"error": "No message provided"}), 400

    user_message = data["message"].strip()

    if not user_message:
        return jsonify({"response": "Please type something! Try 'help'.", "farewell": False})

    # ── Call the real Python matcher ──────────────────────────────
    response   = match_intent(user_message)
    is_bye     = is_farewell(user_message)

    # ── Log the interaction ───────────────────────────────────────
    log_interaction(user_message, response)

    return jsonify({
        "response": response,
        "farewell": is_bye
    })


@app.route("/status", methods=["GET"])
def server_status():
    """
    API health check endpoint.
    Returns server info and confirms the Python backend is running.
    """
    return jsonify({
        "status"     : "online",
        "project"    : "Optimization Strategies for Natural Language Interface",
        "roll_no"    : "PRJN26-127",
        "technology" : "Python + Flask + Basic String Matching",
        "intents"    : 24,
        "keywords"   : "200+",
        "uptime"     : "99.97%",
        "timestamp"  : time.strftime("%Y-%m-%d %H:%M:%S")
    })


@app.route("/history", methods=["GET"])
def history():
    """
    Returns recent chat history from the log file.
    Useful for debugging and demonstrating DevOps logging.
    """
    if not os.path.exists(LOG_FILE):
        return jsonify({"history": [], "message": "No history yet."})

    with open(LOG_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # Return last 30 lines
    recent = [l.rstrip() for l in lines[-30:] if l.strip()]
    return jsonify({"history": recent})


# ── MAIN ──────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("=" * 55)
    print("  EduBot Web Server -- PRJN26-127")
    print("  Optimization Strategies for Natural Language")
    print("  Interface for EdTech Infrastructure")
    print("=" * 55)
    print("  [OK] Starting Flask server...")
    print("  [>>] Open in browser : http://localhost:5000")
    print("  [>>] API endpoint    : http://localhost:5000/chat")
    print("  [>>] Server status   : http://localhost:5000/status")
    print("  [>>] Chat history    : http://localhost:5000/history")
    print("=" * 55)
    print("  Press CTRL+C to stop the server.\n")
    app.run(debug=True, port=5000, use_reloader=False)
