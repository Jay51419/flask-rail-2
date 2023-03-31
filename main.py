from flask import Flask, jsonify,request
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return "Jz Here"

@app.route('/upload',method=["POST"])
def upload():
    data = request.files
    return data["file"]


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
