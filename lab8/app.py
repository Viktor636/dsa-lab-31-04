from flask import Flask, request, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import json
import os

app = Flask(__name__)

# Настройка лимита запросов
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["100 per day"]
)

DATA_FILE = "data.json"

# Загрузка данных при старте приложения
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
else:
    data = {}

def save_data():
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

@app.route("/set", methods=["POST"])
@limiter.limit("10 per minute")
def set_key():
    content = request.get_json()
    key = content.get("key")
    value = content.get("value")
    if not key:
        return jsonify({"error": "key required"}), 400
    data[key] = value
    save_data()
    return jsonify({"status": "ok", "key": key, "value": value})

@app.route("/get/<key>", methods=["GET"])
def get_key(key):
    if key in data:
        return jsonify({"key": key, "value": data[key]})
    return jsonify({"error": "key not found"}), 404

@app.route("/delete/<key>", methods=["DELETE"])
@limiter.limit("10 per minute")
def delete_key(key):
    if key in data:
        del data[key]
        save_data()
        return jsonify({"status": "ok", "deleted": key})
    return jsonify({"error": "key not found"}), 404

@app.route("/exists/<key>", methods=["GET"])
def exists_key(key):
    return jsonify({"key": key, "exists": key in data})

if __name__ == "__main__":
    app.run(debug=True)