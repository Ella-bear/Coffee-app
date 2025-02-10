# flask.py

from flask import Flask, request, jsonify
from home import COFFEE_OPTIONS, place_order
from signin import sign_up, sign_in, USER_DB

# Create the Flask app
app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Welcome to the Coffee Chatbot API!"

@app.route("/signup", methods=["POST"])
def signup():
    data = request.json
    email = data.get("email")
    phone = data.get("phone")
    if not email or not phone:
        return jsonify({"status": "error", "message": "Email and phone are required."}), 400
    
    result = sign_up(email, phone)
    return jsonify(result)

@app.route("/signin", methods=["POST"])
def signin():
    data = request.json
    email = data.get("email")
    phone = data.get("phone")
    if not email or not phone:
        return jsonify({"status": "error", "message": "Email and phone are required."}), 400
    
    result = sign_in(email, phone)
    return jsonify(result)

@app.route("/place-order", methods=["POST"])
def order():
    data = request.json
    email = data.get("email")
    coffee_choice = data.get("coffee_choice")
    pairing_choice = data.get("pairing_choice")
    
    if not email or not coffee_choice:
        return jsonify({"status": "error", "message": "Email and coffee choice are required."}), 400
    
    result = place_order(email, coffee_choice, pairing_choice)
    return jsonify(result)

@app.route("/menu", methods=["GET"])
def menu():
    return jsonify(COFFEE_OPTIONS)

@app.route("/user-orders/<email>", methods=["GET"])
def user_orders(email):
    if email in USER_DB:
        return jsonify(USER_DB[email]["orders"])
    return jsonify({"status": "error", "message": "User not found."}), 404

@app.route("/exit", methods=["GET"])
def exit_app():
    return "Thank you for using the Coffee Chatbot API!"

if __name__ == "__main__":
    app.run(debug=True)