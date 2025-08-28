
# from maths_module import is_even, is_positive
from maths_module import *


num=int(input("Enter the number : "))
if is_even(num):
    print(num," is even")
else:
    print(num," is odd")

num=int(input("Enter the number : "))
if is_positive(num):
    print(num," is positive")
else:
    print(num," is not positive")
