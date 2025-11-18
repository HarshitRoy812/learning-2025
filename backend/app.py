from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/hello', methods=["GET"])
def hello():
    return jsonify({"message": "Hello  !!!"})

@app.route('/', methods=["GET"])
def home():
    return jsonify({"message": "This will be my home page content"})

# Add a middleware to authenticate user request before delivering data

# Brand name

# Navigation - Home, Contact

# Body - It should deliver with respect to page. hint - different content for Home and different content for contact 

# Year and copyright info



if __name__ == "__main__":
    app.run(debug=True)