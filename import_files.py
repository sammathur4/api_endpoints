from flask import Flask, request, jsonify

app = Flask(__name__)

# Dummy data to simulate a database
data = [
    {"id": 1, "name": "Item 1"},
    {"id": 2, "name": "Item 2"},
]
