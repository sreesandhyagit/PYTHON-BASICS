print("\n----Arithmetic Calculator---\n")
print("\t1. Addition\n\t2. Subtraction\n\t3. Multiplication\n\t4. Division\n")
choice = int(input("Please enter your choice (1/2/3/4) : "))
if choice>=1 and choice<=4:
    num1 = float(input("Enter First Number : "))
    num2 = float(input("Enter Second number : "))
    if choice==1:
        print(f"{num1} + {num2} = {num1+num2}")
    elif choice==2:
        print(f"{num1} - {num2} = {num1-num2}")
    elif choice==3:
        print(f"{num1} x {num2} = {num1*num2}")
    else:
        if num2==0:
            print("Division by zero error!!")
        else:
            print(f"{num1} / {num2} = {num1/num2}")
else:
    print("Invalid choice")

