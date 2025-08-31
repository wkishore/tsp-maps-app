from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # ✅ allow requests from frontend

@app.route("/api/hello")
def hello():
    return jsonify({"message": "Hello from backend!"})

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)