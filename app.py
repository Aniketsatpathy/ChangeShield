from flask import Flask
import random
app = Flask(__name__)

@app.route("/health")
def health():
    if random.random() < 0.4:
        return {"status": "error"}, 500
    return {"status": "ok"}, 200

@app.route("/")
def home():
    return "App v2 – Risky Release", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)