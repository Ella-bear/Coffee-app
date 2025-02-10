# main.py

from home import BROWN, CREAM_WHITE, RESET, place_order, recommend_coffee, display_menu
from signin import sign_in, sign_up
from utils import print_welcome_message, print_exit_message

def get_service_choice():
    while True:
        try:
            choice = int(input(f"\n{BROWN}What would you like to do?{RESET}\n1. Place an order\n2. View the menu\n3. Get a recommendation\n4. Exit\n{CREAM_WHITE}Enter your choice (1-4): {RESET}"))
            if choice in [1, 2, 3, 4]:
                return choice
            else:
                print(f"{CREAM_WHITE}Invalid choice. Please enter a number between 1 and 4.{RESET}")
        except ValueError:
            print(f"{CREAM_WHITE}Invalid input. Please enter a number between 1 and 4.{RESET}")

def main():
    print_welcome_message()

    # Step 1: Sign-in or Sign-up
    while True:
        action = input(f"\n{BROWN}Do you want to sign in (s) or sign up (u)?{RESET} ").strip().lower()
        if action == "s":
            email = sign_in()
            if email:
                break
        elif action == "u":
            email = sign_up()
            if email:
                break
        else:
            print(f"{CREAM_WHITE}Invalid choice. Please type 's' for sign in or 'u' for sign up.{RESET}")
    
    while True:
        # Step 2: Ask the user what service they want
        service_choice = get_service_choice()

        if service_choice == 1:  # Place an order
            coffee_choice = input(f"{BROWN}Enter your coffee choice: {RESET}").strip().lower()
            pairing_choice = input(f"{BROWN}Enter your pairing choice (optional): {RESET}").strip().lower()
            result = place_order(email, coffee_choice, pairing_choice)
            print(result["message"])
        
        elif service_choice == 2:  # View the menu
            display_menu()
        
        elif service_choice == 3:  # Get a recommendation
            recommended_coffee = recommend_coffee()
            print(recommended_coffee["message"])
            if recommended_coffee:
                coffee_choice = recommended_coffee["message"].split(": ")[1]
                pairing_choice = input(f"{BROWN}Enter your pairing choice (optional): {RESET}").strip().lower()
                result = place_order(email, coffee_choice, pairing_choice)
                print(result["message"])
        
        elif service_choice == 4:  # Exit
            print_exit_message()
            break

if __name__ == "__main__":
    main()