s="My name is Sreesandhya"
# s[1]='e'  #no change..immutable
# s=s+" Python"
# print(s)
s.lower() # return value not work
print(s)

print(s.lower())
print(s.upper())
print(s.swapcase())
print(s.capitalize())
print(s.split())
print(s)

print(s.index('i'))
print(s.count('s')) # case sensitive
print(s.startswith('M'))
print(s.startswith('m'))
print(s.endswith('a'))
print(s.endswith('y'))

print("My name is Anjali I am 34 years old".format())

name="Neha"
age=25
print(f"My name is {name} I am {age} years old".format())

name="Shalu"
age=27
print("My name is {} I am {} years old".format(name,age))


print(s.partition('is')) # part as in 3 part

print("-".join(s))

print("python".islower())
print("python".isalpha())

print("python34".isalnum())

print("23".isnumeric())

course = "    python" # removes starting spaces
print(course)
print(course.strip())






