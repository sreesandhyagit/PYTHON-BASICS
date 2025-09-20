# Bank Management System

import pickle
from abc import ABC, abstractmethod

def LoginRequired(login):
    def wrapper(user_name,password,status):
        if status:
            login(user_name,password,status)
        else:
            print("Invalid User!!")
    return wrapper

@LoginRequired
def Dashboard(user,password,is_authenticated):    
    print(f"Welcome {user}..You are logged in MYBank")
 
def menu():
    print("========MYBank========")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Search Account")
    print("5. Display All Accounts")
    print("6. Total Bank Balance")
    print("7. Bank Rules")
    print("0. Logout")

def save_data():
    with open("Account_Details.pkl","wb") as file:
        pickle.dump(Bank.accounts,file)       

def load_data():
    try:
        with open("Account_Details.pkl","rb") as file:
            Bank.accounts = pickle.load(file)
    except (FileNotFoundError,EOFError):
        Bank.accounts = {}

class Account(ABC):
    def __init__(self,acc_no,name,balance,email,phone,acc_type):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance
        self.email = email
        self.phone = phone
        self.acc_type = acc_type

    @abstractmethod
    def display_account(self):
        pass

class Savings(Account):
    def __init__(self,acc_no,name,balance,email,phone,acc_type):
        super().__init__(acc_no,name,balance,email,phone,acc_type)
    
    def display_account(self):
        pass

class Current(Account):
    def __init__(self,acc_no,name,balance,email,phone,acc_type):
        super().__init__(acc_no,name,balance,email,phone,acc_type)
    
    def display_account(self):
        pass

class Bank:
    accounts = {}
    def __init__(self,acc_no,name,balance,email,phone,acc_type):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance
        self.email = email
        self.phone = phone
        self.acc_type = acc_type

    @classmethod
    def add_account(cls,acc_no,name,balance,email,phone,acc_type):
        if acc_type == "Savings Account":
                acc = Savings(acc_no,name,balance,email,phone,acc_type)
        else:
                acc = Current(acc_no,name,balance,email,phone,acc_type)
        cls.accounts[acc_no] = acc
        print("Account Created Successfully...!")
        return acc


def create_account():
    acc_no = int(input("Enter account number (4-6 digits): "))
    name = input("Enter name: ")
    balance = float(input("Enter initial balance: "))
    email = input("Enter email: ")
    phone = int(input("Enter phone number(10 digits): "))
    accType= input("Enter account type (s for Savings Account/c for Current Account):")
    acc_type = "Savings Account" if accType.lower() == "s" else "Current Account"
    acc = Bank.add_account(acc_no,name,balance,email,phone,acc_type)  
    if acc:
        save_data()




#  Start Program
while True:
    print("========MYBank========")
    print("Bank Management System")
    print("======================")
    print("\tLogin")
    print("----------------------")
    user_name = input("User Name\t: ")
    password = input("Password\t: ")
    status = True if user_name=="user1" and password=="123" else False
    Dashboard(user_name,password,status)
    if status:
        load_data()
        while True:
            menu()
            choice = int(input("Enter your choice: "))
            match choice:
                case 1: 
                    create_account()
                case 2:
                    pass
                case 3:
                    pass
                case 4:
                    pass
                case 5:
                    pass
                case 6:
                    pass
                case 7:
                    pass
                case 0:
                    print("Logout Successful!")
                    break
                case ___:
                    print("Invalid Choice!!")
                    continue
    
    repeat =input("Do you want to relogin (Enter y for yes):")
    if repeat.lower() == "y":
        continue
    else:
        print("Exiting...Thank you for banking with us!")
        break






