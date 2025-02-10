# payment.py

# ANSI color codes for formatting
BROWN = "\033[38;5;136m"  # Brown color
CREAM_WHITE = "\033[38;5;255m"  # Cream white color
RESET = "\033[0m"  # Reset to default color

# Function to process card payment
def process_card_payment(total_price):
    print(f"\n{BROWN}Processing card payment...{RESET}")
    card_number = input("Enter your card number (16 digits): ").strip()
    if len(card_number) == 16 and card_number.isdigit():
        print(f"{BROWN}Card payment successful! Total paid: ${total_price:.2f}{RESET}")
        return True
    else:
        print(f"{CREAM_WHITE}Invalid card number. Payment failed.{RESET}")
        return False

# Function to process cash payment
def process_cash_payment(total_price):
    print(f"\n{BROWN}Processing cash payment...{RESET}")
    while True:
        try:
            cash_given = float(input(f"Enter the amount of cash given (${total_price:.2f} required): ").strip())
            if cash_given >= total_price:
                change = cash_given - total_price
                print(f"{BROWN}Cash payment successful! Your change: ${change:.2f}{RESET}")
                return True
            else:
                print(f"{CREAM_WHITE}Insufficient amount. Please provide at least ${total_price:.2f}.{RESET}")
        except ValueError:
            print(f"{CREAM_WHITE}Invalid input. Please enter a valid amount.{RESET}")

# Function to handle payment
def handle_payment(total_price):
    while True:
        payment_method = input(f"\nWould you like to pay by 'card' or 'cash'?{RESET} ").strip().lower()
        if payment_method == "card":
            if process_card_payment(total_price):
                return payment_method
        elif payment_method == "cash":
            if process_cash_payment(total_price):
                return payment_method
        else:
            print(f"{CREAM_WHITE}Invalid payment method. Please choose 'card' or 'cash'.{RESET}")