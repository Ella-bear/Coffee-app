# home.py

import random

# ANSI color codes for formatting
BROWN = "\033[38;5;136m"  # Brown color
CREAM_WHITE = "\033[38;5;255m"  # Cream white color
RESET = "\033[0m"  # Reset to default color

# Sample data for the chatbot
COFFEE_OPTIONS = {
    "espresso": {"price": 2.50, "pairing_suggestions": ["croissant", "muffin"]},
    "latte": {"price": 3.50, "pairing_suggestions": ["cookie", "brownie"]},
    "cappuccino": {"price": 3.00, "pairing_suggestions": ["danish pastry", "scone"]},
    "americano": {"price": 3.00, "pairing_suggestions": ["bagel", "donut"]},
    "macchiato": {"price": 3.20, "pairing_suggestions": ["chocolate chip cookie", "slice of cake"]},
    "ice coffee": {"price": 3.00, "pairing_suggestions": ["ice cream", "brownie"]},
}

PAIRING_ITEMS = {
    "croissant": 2.00,
    "muffin": 1.75,
    "cookie": 1.50,
    "brownie": 2.25,
    "danish pastry": 2.50,
    "scone": 2.00,
    "bagel": 1.75,
    "donut": 1.50,
    "chocolate chip cookie": 1.50,
    "slice of cake": 3.00,
    "ice cream": 2.50,
}

# Function to display the menu
def display_menu():
    print(f"\n{BROWN}Here's our menu:{RESET}")
    for coffee, details in COFFEE_OPTIONS.items():
        print(f"- {coffee.capitalize()} (${details['price']:.2f})")

# Function to place an order
def place_order(email, coffee_choice, pairing_choice=None):
    if coffee_choice not in COFFEE_OPTIONS:
        return {"status": "error", "message": "Invalid coffee choice."}
    
    coffee_price = COFFEE_OPTIONS[coffee_choice]["price"]
    pairing_price = PAIRING_ITEMS.get(pairing_choice, 0)
    total_price = coffee_price + pairing_price
    
    # Simulate payment success (no user input in API mode)
    payment_method = "card"  # Default payment method for API
    order_summary = {
        "coffee": coffee_choice,
        "pairing": pairing_choice,
        "total": total_price,
        "payment_method": payment_method
    }
    
    from signin import USER_DB
    if email not in USER_DB:
        USER_DB[email] = {"orders": []}
    USER_DB[email]["orders"].append(order_summary)
    return {
        "status": "success",
        "message": f"Order placed successfully! Total: ${total_price:.2f}",
        "order_summary": order_summary
    }

# Function to recommend a coffee
def recommend_coffee():
    recommended_coffee = random.choice(list(COFFEE_OPTIONS.keys()))
    return {"status": "success", "message": f"Suggested coffee: {recommended_coffee}"}