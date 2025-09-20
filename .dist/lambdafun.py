"""
def Square(num):
    return num**2 

print(Square(5))
"""
"""
d=lambda num:num**2
print(d(4))

add=lambda a,b:a+b
print(add(43,2))

"""
"""
def Is_Evan(num):
    if num%2==0:
        return num
    else:
        return ""

for k in range(2,51):
    print(Is_Evan(k))
"""

def Square(num):
    return num**2

for k in range(2,6):
    print(Square(k))

print(map(Square,range(2,6)))
print(list(map(Square,range(2,6))))
print(tuple(map(Square,range(2,6))))
print(set(map(Square,range(2,6))))#unordered

Square=lambda num:num**2
print(list(map(Square,range(3,9))))

print(tuple(map(lambda num:num**2,[2,3,7,8])))

print(list(map(lambda a: a%2==0,(56,12,7,9,23))))

print(list(filter(lambda a: a%2==0,(56,12,7,9,23,78))))

first_name=["Sandhya","Athulya"]
last_name=["Ajesh","Roshan"]

print(list(map(lambda f_name,l_name:f_name+" "+l_name,first_name,last_name)))
"""
"""
#  sum of list of numbers

from functools import reduce
s=reduce(lambda a,b:a+b,[3,6,12,8])
print(s)

# factorial
print(reduce(lambda a,b:a*b,range(1,6)))


