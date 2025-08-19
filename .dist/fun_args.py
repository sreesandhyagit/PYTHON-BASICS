"""def fun(n,a):
    print(f"My name is {n} and I am {a} years old")

name="Adi"
age=12
fun(a=age,n=name)
"""
"""
def Add(*number):
    sum=0
    for k in number:
        sum+=k
    return sum
    
print("Sum of numbers is ",Add(1,2,3,4,5))
"""
"""
def fun(**kwargs):
    print(kwargs)
    print(f"My name is {kwargs['n']} and I am {kwargs['a']}")
    print("Live in",kwargs['place'])

name="Edwin"
age=27

fun(a=age,n=name,place="kochi")

"""
"""
def fun(n,a,p='Kochi'):
    print(f"My name is {n} and I am {a} years old")
    print("I live in ",p)

name=input("Enter your name : ")
age=input("Enter your age : ")

fun(name,age,p="Kozhikode")

"""
def Sum(num):
    if num==0:
        return 0
    else:
        return num+Sum(num-1)
    
num=5
print(f"Sum of {num} number is {Sum(num)}")

