# from mypackages.maths_module import is_even

from mypackages import maths_module


num=int(input("Enter the number : "))
if maths_module.is_even(num):
    print(num," is even")
else:
    print(num," is odd")

num=int(input("Enter the number : "))
if maths_module.is_positive(num):
    print(num," is positive")
else:
    print(num," is not positive")
