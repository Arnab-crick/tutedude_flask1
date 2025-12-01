from flask import Flask, jsonify
import json

app = Flask(__name__)
DATA_FILE = "data.json"

@app.route("/api", methods=["GET"])
def api():
    # Read backend file
    with open(DATA_FILE, "r") as f:
        data = json.load(f)

    # Return the entire JSON list exactly as stored
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
