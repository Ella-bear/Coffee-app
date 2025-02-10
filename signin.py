# signin.py

import re

# ANSI color codes for formatting
BROWN = "\033[38;5;136m"  # Brown color
CREAM_WHITE = "\033[38;5;255m"  # Cream white color
RESET = "\033[0m"  # Reset to default color

# Simulated user database
USER_DB = {}

# Function to validate email
def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None

# Function to validate phone number
def is_valid_phone(phone):
    return re.match(r"^\+?\d{10,15}$", phone) is not None

# Function for user sign-up
def sign_up():
    print(f"\n{BROWN}Let's create your account!{RESET}")
    while True:
        email = input("Enter your email: ").strip()
        if is_valid_email(email):
            if email in USER_DB:
                print(f"{CREAM_WHITE}This email is already registered. Please log in.{RESET}")
                return None
            break
        else:
            print(f"{CREAM_WHITE}Invalid email format. Please try again.{RESET}")
    
    while True:
        phone = input("Enter your phone number: ").strip()
        if is_valid_phone(phone):
            break
        else:
            print(f"{CREAM_WHITE}Invalid phone number format. Please try again.{RESET}")
    
    USER_DB[email] = {"phone": phone, "orders": []}
    print(f"{BROWN}Account created successfully!{RESET}")
    return email

# Function for user sign-in
def sign_in():
    print(f"\n{BROWN}Welcome back! Please sign in.{RESET}")
    while True:
        email = input("Enter your email: ").strip()
        if email in USER_DB:
            phone = input("Enter your phone number: ").strip()
            if phone == USER_DB[email]["phone"]:
                print(f"{BROWN}Signed in successfully!{RESET}")
                return email
            else:
                print(f"{CREAM_WHITE}Phone number does not match. Please try again.{RESET}")
        else:
            print(f"{CREAM_WHITE}Email not found. Please sign up first.{RESET}")
            return None