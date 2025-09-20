import re
import pickle
from functools import reduce
from datetime import datetime


# ---------------------------
# Decorator for transaction logs
# ---------------------------
def log_transaction(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG] {func.__name__.upper()} called at {datetime.now()}")
        return func(*args, **kwargs)
    return wrapper


# ---------------------------
# Account Class
# ---------------------------
class Account:
    bank_name = "Python Bank"
    accounts = {}  # {acc_no: Account object}

    def __init__(self, acc_no, name, email, balance=0):
        self.__acc_no = acc_no
        self.__name = name
        self.__email = email
        self.__balance = balance

    # Encapsulation: getters
    def get_acc_no(self):
        return self.__acc_no

    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

    def get_balance(self):
        return self.__balance

    # Operator Overloading: Merge balances
    def __add__(self, other):
        return self.__balance + other.__balance

    # Deposit
    @log_transaction
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"₹{amount} deposited. New Balance: ₹{self.__balance}")
        else:
            print("Invalid deposit amount!")

    # Withdraw
    @log_transaction
    def withdraw(self, amount):
        try:
            if amount <= 0:
                raise ValueError("Invalid withdrawal amount!")
            if self.__balance >= amount:
                self.__balance -= amount
                print(f"₹{amount} withdrawn. New Balance: ₹{self.__balance}")
            else:
                raise ValueError("Insufficient balance!")
        except ValueError as e:
            print("Error:", e)

    # Display
    def display(self):
        print(f"Acc No: {self.__acc_no}, Name: {self.__name}, Email: {self.__email}, Balance: ₹{self.__balance}")

    # Class Method for account creation
    @classmethod
    def create_account(cls, acc_no, name, email, balance=0):
        if not re.match(r"^[0-9]{4,6}$", str(acc_no)):
            print("Invalid Account Number! Must be 4-6 digits.")
            return None
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            print("Invalid Email ID!")
            return None

        acc = Account(acc_no, name, email, balance)
        cls.accounts[acc_no] = acc
        print("Account created successfully!")
        return acc

    # Static Method
    @staticmethod
    def bank_rules():
        print("Bank Rules: Minimum balance ₹500, No overdraft allowed.")


# ---------------------------
# File Handling
# ---------------------------
def save_data():
    with open("accounts.pkl", "wb") as f:
        pickle.dump(Account.accounts, f)


def load_data():
    try:
        with open("accounts.pkl", "rb") as f:
            Account.accounts = pickle.load(f)
    except (FileNotFoundError, EOFError):
        Account.accounts = {}


# ---------------------------
# Menu Functions
# ---------------------------
def create_account():
    acc_no = input("Enter Account Number (4-6 digits): ")
    name = input("Enter Name: ")
    email = input("Enter Email: ")
    balance = float(input("Enter Initial Deposit: "))

    acc = Account.create_account(acc_no, name, email, balance)
    if acc:
        save_data()


def deposit_money():
    acc_no = input("Enter Account Number: ")
    if acc_no in Account.accounts:
        amount = float(input("Enter Amount to Deposit: "))
        Account.accounts[acc_no].deposit(amount)
        save_data()
    else:
        print("Account not found!")


def withdraw_money():
    acc_no = input("Enter Account Number: ")
    if acc_no in Account.accounts:
        amount = float(input("Enter Amount to Withdraw: "))
        Account.accounts[acc_no].withdraw(amount)
        save_data()
    else:
        print("Account not found!")


def display_account():
    acc_no = input("Enter Account Number: ")
    if acc_no in Account.accounts:
        Account.accounts[acc_no].display()
    else:
        print("Account not found!")


def display_all_accounts():
    if not Account.accounts:
        print("No accounts available.")
    else:
        for acc in Account.accounts.values():
            acc.display()


def calculate_total_balance():
    balances = [acc.get_balance() for acc in Account.accounts.values()]
    total = reduce(lambda x, y: x + y, balances, 0)
    print(f"Total Balance in Bank: ₹{total}")


# ---------------------------
# Main Program
# ---------------------------
def main():
    load_data()
    while True:
        print("\n----- Python Bank Management -----")
        print("1. Create Account")
        print("2. Deposit") 
        print("3. Withdraw")
        print("4. Display Account")
        print("5. Display All Accounts")
        print("6. Calculate Total Bank Balance")
        print("7. Bank Rules")
        print("0. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            create_account()
        elif choice == "2":
            deposit_money()
        elif choice == "3":
            withdraw_money()
        elif choice == "4":
            display_account()
        elif choice == "5":
            display_all_accounts()
        elif choice == "6":
            calculate_total_balance()
        elif choice == "7":
            Account.bank_rules()
        elif choice == "0":
            print("Exiting... Thank you for banking with us!")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()