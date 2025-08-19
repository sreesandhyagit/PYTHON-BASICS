"""
while condition:
    statements
    """
"""""count=1
while count<=5:
    print(count)
    count=count+1
    """""
# factorial
"""
fact=1;
n=int(input("Enter an integer number"))
i=1
while i<=n:
    fact=fact*i
    i=i+1
print(f"Factorial of {n} is {fact}")

"""
"""
n=int(input("Enter how many fibonacci series"))
a,b=0,1
print(a,b,end=" ")
c=1
while c<=n:
    t=a+b
    print(t,end=" ")
    a,b=b,t
    c=c+1
"""
# Arithmetic Calculator

while True:
    print("\n----Arithmetic Calculator---\n")
    num1 = int(input("Enter First Number : "))
    num2 = int(input("Enter Second number : "))
    print("\t1. Addition\n\t2. Subtraction\n\t3. Multiplication\n\t4. Division\n")
    choice = int(input("Please enter your choice (1/2/3/4) : "))
    match choice:
        case 1:
            print(f"{num1} + {num2} = {num1+num2}")
        case 2:
            print(f"{num1} - {num2} = {num1-num2}")
        case 3: 
            print(f"{num1} x {num2} = {num1*num2}")
        case 4:
            if num2==0:
                print("Division by zero error!!")
            else:
                print(f"{num1} / {num2} = {num1/num2}")
        case __: 
            print("Invalid choice")
    opt=input("Do you wish to continue (yes/no) : ")
    if opt=="yes":
        continue
    else:
        break


