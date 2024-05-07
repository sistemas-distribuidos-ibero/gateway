# dependencies -------->
from flask import Flask, jsonify
from dotenv import load_dotenv
from requests import post
import os

# program initialization -------->
load_dotenv()

# program variables -------->
app = Flask(__name__)

# end points -------->
# authentication endpoints
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    if not data or 'email' not in data or 'password' not in data:
        return jsonify({'error': 'Missing data'}), 400
    # consume the login service
    response = post(os.environ['AUTH_SERVICE']+'/register', json=data)
    return jsonify(response.json()), response.status_code

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    if not data or 'email' not in data or 'password' not in data:
        return jsonify({'error': 'Missing data'}), 400
    # consume the login service
    response = post(os.environ['AUTH_SERVICE']+'/login', json=data)
    return jsonify(response.json()), response.status_code

# program execution -------->
if __name__ == "__main__":
    app.run(debug=True, port=6789)
