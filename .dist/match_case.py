print("\n----Arithmetic Calculator---\n")

print("\t1. Addition\n\t2. Subtraction\n\t3. Multiplication\n\t4. Division\n")
choice = int(input("Please enter your choice (1/2/3/4) : "))
match choice:
    case 1:
        num1 = float(input("Enter First Number : "))
        num2 = float(input("Enter Second number : "))
        print(f"{num1} + {num2} = {num1+num2}")
    case 2:
        num1 = float(input("Enter First Number : "))
        num2 = float(input("Enter Second number : "))
        print(f"{num1} - {num2} = {num1-num2}")
    case 3: 
        num1 = float(input("Enter First Number : "))
        num2 = float(input("Enter Second number : "))
        print(f"{num1} x {num2} = {num1*num2}")
    case 4:
        num1 = float(input("Enter First Number : "))
        num2 = float(input("Enter Second number : "))
        if num2==0:
            print("Division by zero error!!")
        else:
            print(f"{num1} / {num2} = {num1/num2}")
    case __: 
        print("Invalid choice")


