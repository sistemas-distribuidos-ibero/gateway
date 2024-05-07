# dependencies -------->
from flask import Flask, jsonify
from dotenv import load_dotenv
from requests import post, get, put, delete
import os

# program initialization -------->
load_dotenv()

# program variables -------->
app = Flask(__name__)

# end points -------->

# authentication endpoints --------
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    if not data or 'email' not in data or 'password' not in data:
        return jsonify({'error': 'Missing data'}), 400
    # consume the service
    response = post(os.environ['AUTH_SERVICE']+'/register', json=data)
    return jsonify(response.json()), response.status_code

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    if not data or 'email' not in data or 'password' not in data:
        return jsonify({'error': 'Missing data'}), 400
    # consume the service
    response = post(os.environ['AUTH_SERVICE']+'/login', json=data)
    return jsonify(response.json()), response.status_code

# order endpoints --------
@app.route('/orders', methods=['GET'])
def get_orders():
    # consume the service
    response = get(os.environ['ORDERS_SERVICE']+'/orders')
    return jsonify(response.json()), response.status_code

@app.route('/orders', methods=['POST'])
def create_order():
    data = request.json
    # consume the service
    response = post(os.environ['ORDERS_SERVICE']+'/orders', json=data)
    return jsonify(response.json()), response.status_code

@app.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    # consume the service
    response = get(os.environ['ORDERS_SERVICE']+f'/orders/{order_id}')
    return jsonify(response.json()), response.status_code

@app.route('/orders/<int:order_id>', methods=['PUT'])
def update_order(order_id):
    data = request.json
    # consume the service
    response = put(os.environ['ORDERS_SERVICE']+f'/orders/{order_id}', json=data)
    return jsonify(response.json()), response.status_code

@app.route('/orders/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    # consume the service
    response = delete(os.environ['ORDERS_SERVICE']+f'/orders/{order_id}')
    return jsonify(response.json()), response.status_code

# cart endpoints --------
@app.route('/cart', methods=['POST'])
def add_to_cart():
    data = request.json
    # consume the service
    response = post(os.environ['CART_SERVICE']+'/cart', json=data)
    return jsonify(response.json()), response.status_code

@app.route('/cart', methods=['GET'])
def get_cart():
    data = request.json
    # consume the service
    response = get(os.environ['CART_SERVICE']+'/cart', json=data)
    return jsonify(response.json()), response.status_code

@app.route('/cart', methods=['DELETE'])
def del_cart():
    data = request.json
    # consume the service
    response = delete(os.environ['CART_SERVICE']+'/cart', json=data)
    return jsonify(response.json()), response.status_code

# authentication endpoints --------


# program execution -------->
if __name__ == "__main__":
    app.run(debug=True, port=6789)
