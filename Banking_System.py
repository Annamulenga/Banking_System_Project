#Project: Banking System
#By: Anna Mulenga
#Date: 2025-04-03

# Description:

# This is a simple banking system that allows users to create accounts, deposit and withdraw money, and display account balances.
# It handles exceptions for invalid input and unexpected errors.
# It uses a text file to store account data and loads it at the start of the program.
# The program provides a menu-driven interface for users to interact with the banking system.
# It includes functions to load and save account data, create accounts, deposit and withdraw money, and display balances.
# Importing necessary libraries


import random  # For generating account numbers


def load_accounts():

    try:
        with open("accounts.txt", "r") as file:
            accounts = [line.strip().split(",") for line in file]
    except FileNotFoundError:
        print("Error: accounts.txt not found.")
        accounts = []
    except Exception as e:
        print(f"An unexpected error occurred while loading accounts: {e}")
        accounts = []
    return accounts

def save_accounts(accounts):
    
    try:
        with open("accounts.txt", "w") as file:
            for account in accounts:
                file.write(",".join(account) + "\n")
    except Exception as e:
        print(f"An error occurred while saving accounts: {e}")

''' Creates a new account, generates a unique account number and initializes the balance to 0
    It appends the new account to the accounts list
    It handles exceptions for invalid input and unexpected errors'''


def create_account(accounts):
   
    try:
        name = input("Enter account holder name: ")
        account_number = str(random.randint(1000000000, 9999999999))
        initial_balance = 0.0
        accounts.append([name, account_number, str(initial_balance)])
        print(f"Account successfully created for {name} with account number: {account_number}")
    except Exception as e:
        print(f"An error occurred while creating account: {e}\nPlease try again later.")
    return accounts

''' Finds an account by account number
    It iterates through the accounts list and checks if the account number matches
    If a match is found, it returns the account
    If no match is found, it returns None
    It handles exceptions for invalid input and unexpected errors'''

def find_account(accounts, account_number):
   
    for account in accounts:
        if len(account) > 1 and account[1] == account_number:
            return account
    return None

'''# Deposits money into an existing account
     It retrieves the account number and checks if it exists
     If the account exists, it adds the amount to the account
     If the account does not exist, it prompts the user to try again
     It also checks if the deposit amount is valid (positive number) prompting the user to try again if an invalid amount is entered
     It handles exceptions for invalid input and unexpected errors'''

def deposit(accounts):
   
    account_number = input("Enter account number: ")
    account = find_account(accounts, account_number)
    if not account:
        print("Invalid account number.\n2Please try again.")
        return accounts

    try:
        amount = float(input("Enter deposit amount: "))
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        account[2] = str(float(account[2]) + amount)
        print("Deposit successful.")
    except ValueError as e:
        print(f"Invalid input: {e}")
    except Exception as e:
        print(f"An error occurred during deposit: {e}\nPlease try again.")
    return accounts

''' Withdraws money from an existing account
    It retrieves the account number and checks if it exists
    If the account exists, it checks if there are sufficient funds
    If there are sufficient funds, it deducts the amount from the account
    If there are insufficient funds, it prompts the user to try again '''

def withdraw(accounts):

    account_number = input("Enter account number: ")
    account = find_account(accounts, account_number)
    if not account:
        print("Invalid account number.\nPlease try again.")
        return accounts

    try:
        amount = float(input("Enter withdrawal amount: "))
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if float(account[2]) >= amount:
            account[2] = str(float(account[2]) - amount)
            print("Withdrawal successful.")
        else:
            print("Insufficient funds.")
    except ValueError as e:
        print(f"Invalid input: {e}")
    except Exception as e:
        print(f"An error occurred during withdrawal: {e}\NPlease try again.")
    return accounts

''' Displays the balance of an account
    It retrieves the account number and checks if it exists
    If the account exists, it displays the account holder's name and balance
    If the account does not exist, it prompts the user to try again'''

def display_balance(accounts):
    account_number = input("Enter account number: ")
    account = find_account(accounts, account_number)
    if not account:
        print("Invalid account number.\nPlease try again.")
        return accounts

    try:
        print(f"Account holder: {account[0]}, Balance: {account[2]}")
    except Exception as e:
        print(f"An error occurred while displaying balance: {e}\nPlease try again.")
    return accounts

''' The main function to run the banking system
    It includes a menu for the user to select options
    and handles the flow of the program'''

def main():
    accounts = load_accounts()

    while True:
        print("\nBANKING SYSTEM\n===================================\n")
        print("Please select an option:\n")
        print("Options:\n")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Display Balance")
        print("5. Exit\n")

        choice = input("Enter choice: ")

        try:
            if choice == "1":
                accounts = create_account(accounts)
            elif choice == "2":
                accounts = deposit(accounts)
            elif choice == "3":
                accounts = withdraw(accounts)
            elif choice == "4":
                accounts = display_balance(accounts)
            elif choice == "5":
                break
            else:
                print("Invalid choice.")
        except ValueError:
            print("Invalid input. Please enter a number.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}\nPlease try again.")
        save_accounts(accounts)

if __name__ == "__main__":
    main()