# backend/app.py
from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongodb://database:27017/")
db = client["webapp"]

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    name = data['name']
    email = data['email']
    db.users.insert_one({"name": name, "email": email})
    return jsonify({"message": "Data submitted successfully!"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
