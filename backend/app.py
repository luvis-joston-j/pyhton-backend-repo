from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB connection
client = MongoClient("mongodb://54.158.172.115:27017/")
db = client["cloth_store"]
collection = db["purchases"]

@app.route('/api/purchase', methods=['POST'])
def add_purchase():
    data = request.json
    if not data:
        return jsonify({"error": "Invalid data"}), 400
    collection.insert_one(data)
    return jsonify({"message": "Purchase added"}), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)

