import re

# # match

# # pattern = "Hello"
# pattern = r"Hello"
# message = "Hello Developers"
# msg = "hello developers"

# print(re.match(pattern,message))
# print(bool(re.match(pattern,message)))

# print(re.match(pattern,msg))
# print(bool(re.match(pattern,msg)))
# print(" ")

# text = "Hello World"
# result = re.match("Hello",text)
# print(result)
# print(" ")

# text = "World Hello"
# result = re.match("Hello",text)
# print(result)
# print(" ")

# pattern = r"\d"
# message = " DeveloHell4opers"
# print(bool(re.match(pattern,message)))
# print(" ")

# pattern = r"\d"
# message = "7DeveloHell4opers"
# print(bool(re.match(pattern,message)))
# print(" ")

# # search 

# text = "World Hello"
# result = re.search("Hello",text)
# print(result)
# print(" ")

# pattern = r"\d"
# message = " DeveloHell4opers"
# print(bool(re.search(pattern,message)))
# print(" ")

# pattern = r"\d"
# message = "7DeveloHell4opers"
# print(bool(re.search(pattern,message)))
# print(" ")

# # findall
# pattern = r"\d"
# message = "7DeveloHell4opers"
# print(re.findall(pattern,message))
# print(" ")

# pattern = r"\d+"
# message = "7DeveloHell423ope56rs"
# print(re.findall(pattern,message))
# print(" ")

# pattern =r"[A-Z]"
# msg = "4Hello Everyone Welcome 2025"
# print(re.findall(pattern,msg))
# print(" ")

# pattern =r"[A-Z0-9]"
# msg = "4Hello Everyone Welcome 2025"
# print(re.findall(pattern,msg))
# print(" ")

# #email validation

# pattern =r"[A-Z0-9a-z]+@[a-zA-Z0-9]+\.(in|com|org|dev)$" 
# email = input("Enter your email : ")
# if re.match(pattern,email):
#     print("Valid")
# else:
#     print("Not valid")
# print("--------------------------------------------")
# pattern =r"[A-Z0-9a-z]{2,}@[a-zA-Z0-9]+\.(in|com|org|dev)$" 
# email = input("Enter your email : ")
# if re.match(pattern,email):
#     print("Valid")
# else:
#     print("Not valid")

#password validation
# pattern = r"(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*\W).{8,}$" # use 1
pattern = r"(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*\w).{8,}$" # use 2
password = input("Enter your password : ")
if re.match(pattern,password):
    print("Valid")
else:
    print("Not valid")