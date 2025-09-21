# Bank Management System

import pickle
# from abc import ABC, abstractmethod
import datetime
from functools import reduce

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

# ==================================================================================================
def log_transactions(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG] {func.__name__.upper()} called at {datetime.datetime.now()}")
        return func(*args, **kwargs)
    return wrapper

def save_data():
    with open("Account_details.pkl","wb") as file:
        pickle.dump(Bank.accounts,file)       

def load_data():
    try:
        with open("Account_details.pkl","rb") as file:
            Bank.accounts = pickle.load(file)
    except (FileNotFoundError,EOFError):
        Bank.accounts = {}
# ===================================================================================================
# class Account(ABC):
#     def __init__(self,acc_no,name,balance,email,phone,acc_type):
#         self.acc_no = acc_no
#         self.name = name
#         self.balance = balance
#         self.email = email
#         self.phone = phone
#         self.acc_type = acc_type

#     @abstractmethod
#     def display(self):
#         pass

# class Savings(Account):
#     def __init__(self,acc_no,name,balance,email,phone,acc_type):
#         super().__init__(acc_no,name,balance,email,phone,acc_type)
    
#     def display(self):
#         print("=====Savings Account=====")
#         if self.acc_type == "Savings Account":
#             print(self.acc_no,self.name,self.balance,self.email,self.phone)

# class Current(Account):
#     def __init__(self,acc_no,name,balance,email,phone,acc_type):
#         super().__init__(acc_no,name,balance,email,phone,acc_type)
    
#     def display(self):
#         print("=====Current Account=====")
#         if self.acc_type == "Current Account":
#                 print(self.acc_no,self.name,self.balance,self.email,self.phone)

# ===================================================================================================
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
        # if acc_type == "Savings Account":
        #         acc = Savings(acc_no,name,balance,email,phone,acc_type)
        # else:
        #         acc = Current(acc_no,name,balance,email,phone,acc_type)
        acc = Bank(acc_no,name,balance,email,phone,acc_type)
        cls.accounts[acc_no] = acc
        print("Account Created Successfully...!")
        return acc
    
    @log_transactions
    def deposit_amount(self,amount):
        if amount>0:
            self.balance +=amount
            print(f"{amount} deposited successfully!")
            print(f"New balance: {self.balance}")
        else:
            print("Invalid deposit amount!!")

    @log_transactions
    def withdraw_amount(self,amount):
        try:
            if amount<0:
                raise ValueError("Invalid withdrawal amount!")
            if self.balance>=amount:
                self.balance -= amount
                print(f"{amount} withdrawn successfully!")
                print(f"New balance: {self.balance}")
            else:
                raise ValueError("Insufficient balance!")
        except ValueError as e:
            print("Error : ",e)
    
    def display_account(self):
        print(f"Account Number: {self.acc_no} Name: {self.name} Email: {self.email} Phone: {self.phone} Account Type: {self.acc_type} Balance: {self.balance}")
    # def dispaly_all_accounts(self):        
        # sa = Savings(self.acc_no,self.name,self.balance,self.email,self.phone,self.acc_type)
        # sa.display_savings_account()
        # ca = Current(self.acc_no,self.name,self.balance,self.email,self.phone,self.acc_type)
        # ca.display_current_account()

    def __add__(self,other):
        return self.balance + other.balance
    
    def get_balance(self):
        return self.balance
    
    @staticmethod
    def bank_rules():
        print("Minimum balance : 500")
    

# ====================================================================================================
def create_account():
    acc_no = int(input("Enter account number (4-6 digits): "))
    name = input("Enter name: ")
    balance = float(input("Enter initial balance: "))
    email = input("Enter email: ")
    phone = int(input("Enter phone number(10 digits): "))
    acc_type= input("Enter account type (s for Savings Account/c for Current Account):")
    acc_type = "Savings Account" if acc_type.lower() == "s" else "Current Account"
    acc = Bank.add_account(acc_no,name,balance,email,phone,acc_type)  
    if acc:
        save_data()

def deposit():
    acc_no = int(input("Enter account number : "))
    if acc_no in Bank.accounts:
       amount = float(input("Enter deposit amount: "))
       Bank.accounts[acc_no].deposit_amount(amount)
       save_data()
    else:
        print("Account not found!!")

def withdraw():
    acc_no = int(input("Enter account number : "))
    if acc_no in Bank.accounts:
       amount = float(input("Enter withdrawal amount: "))
       Bank.accounts[acc_no].withdraw_amount(amount)
       save_data()
    else:
        print("Account not found!!")

def search():
    acc_no = int(input("Enter account number: "))
    if acc_no in Bank.accounts:
        Bank.accounts[acc_no].display_account()
    else:
        print("Account not found!!")

def display_all():
    if not Bank.accounts:
        print("Accounts not found!!")
    else:
        for acc in Bank.accounts.values():
            acc.display_account()

def total_bank_balance():
    balances = [acc.get_balance() for acc in Bank.accounts.values()]
    total = reduce(lambda x,y:x+y,balances,0)
    print("Total balance in the bank:",total)


 
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

# ====================================================================================================
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
                    deposit()
                case 3:
                    withdraw()
                case 4:
                    search()
                case 5:
                    display_all()
                case 6:
                    total_bank_balance()
                case 7:
                    Bank.bank_rules()
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






