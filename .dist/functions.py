"""def Greeting():
    print("Hello Sreesandhya..")
    print("Good evening...")
Greeting()
Greeting()
"""
"""
def Greeting(name): # parameters
    print(f"Hello {name}")

Greeting("Sreesandhya") # arguments
Greeting("Ajesh")
Greeting("Aditya")
"""
"""
def is_even(num):
    if num%2==0:
        print("Even")
    else:
        print("Odd")

is_even(7)
is_even(8)
"""
"""
def fun(n,a):
    print(f"My name is {name} and I am {age} years old")

name=input("Enter your name : ")
age=int(input("Enter the age :"))
fun(name,age)
"""
"""
def Total(l):
    sum=0
    for k in l:
        sum+=k
    print(sum)

Total([45,12,6])
n=[1,2,3,4,5]
Total(n)
"""
"""
def Total(l):
    sum=0
    for k in l:
        sum+=k
    return sum

print(Total([45,12,6]))
n=[1,2,3,4,5]
t=Total(n)
print("Average = ",t/len(n))
"""

def is_Even(num):
    if num%2==0:
        return True
    else:
        return False
    
number=22
if is_Even(number):
    print(number," is even")
else:
    print(number," is odd")

