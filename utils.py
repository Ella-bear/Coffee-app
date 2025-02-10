# utils.py

# ANSI color codes for formatting
BROWN = "\033[38;5;136m"  # Brown color
CREAM_WHITE = "\033[38;5;255m"  # Cream white color
RESET = "\033[0m"  # Reset to default color

# Function to print a welcome message
def print_welcome_message():
    print(f"{BROWN}Welcome to the Coffee Chatbot! Let's get started.{RESET}")

# Function to exit the application
def print_exit_message():
    print(f"{BROWN}Thank you for visiting! Have a great day!{RESET}")