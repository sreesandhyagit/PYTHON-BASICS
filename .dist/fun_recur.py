"""
def Fun():
    print("Hello")
    Fun()

Fun()
"""
def Factorial(num):
    if num==0:
        return 1
    else:
        return num*Factorial(num-1)

n=5
print(f"Factorial of {n} is {Factorial(n)}")

