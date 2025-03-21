import time
import sys


def view_balance(balance):
    return f"Your balance: {balance} TL"


def withdraw_money(balance, amount):
    if amount > balance:
        return None, "Insufficient balance!"
    return balance - amount, f"{amount} TL has been withdrawn."


def deposit_money(balance, amount):
    return balance + amount, f"{amount} TL has been deposited."


def atm_system():
    password = "1234"
    attempts = 3
    balance = 500
    authenticated = False  # Tracks whether the user has successfully entered the password

    print(("*" * 40 + "  ATM  " + "*" * 40).center(110))

    while True:
        try:
            if not authenticated:  # Only ask for the password if not already authenticated
                user_password = input("\nPlease enter your password: ")

                if user_password == password:
                    authenticated = True
                else:
                    attempts -= 1
                    print(f"Incorrect password! Remaining attempts: {attempts}")
                    if attempts <= 0:
                        print("Your card has been blocked. Please contact your bank.")
                        break
                    continue

            print("\n1- View Balance"
                  "\n2- Withdraw Money"
                  "\n3- Deposit Money"
                  "\n4- Exit")

            choice = input("\nMake a selection: ")
            if not choice.isdigit() or int(choice) not in [1, 2, 3, 4]:
                print("Invalid choice, please try again.")
                continue

            choice = int(choice)

            if choice == 1:
                print("\nLoading account information...")
                time.sleep(0.5)
                print(view_balance(balance))

            elif choice == 2:
                amount = input("\nEnter the amount to withdraw: ")
                if not amount.isdigit():
                    print("Invalid amount, please try again.")
                    continue

                amount = int(amount)
                new_balance, message = withdraw_money(balance, amount)

                if new_balance is None:
                    print(message)
                else:
                    balance = new_balance
                    print(message)
                    print(view_balance(balance))

            elif choice == 3:
                amount = input("\nEnter the amount to deposit: ")
                if not amount.isdigit():
                    print("Invalid amount, please try again.")
                    continue

                amount = int(amount)
                balance, message = deposit_money(balance, amount)
                print(message)
                print(view_balance(balance))

            elif choice == 4:
                print("Returning your card...")
                time.sleep(1)
                break

        except KeyboardInterrupt:
            print("\nLogging out...")
            sys.exit()
        except Exception as e:
            print(f"An error occurred: {e}. Please try again.")


atm_system()
