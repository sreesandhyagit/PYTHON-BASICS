"""
syntax

if condition:
    statements

"""
"""age=30
if age>=18:
    print("Eligible for voting")


if age>=18:
    print("Eligible for voting")
else:
    print("Not eligible for voting")
"""
"""
age=20
print("Eligible for vote") if age>=18 else print("Not eligible for vote")
"""

"""
mark=int(input("Enter your mark : "))
if mark>=95:
    print("Excellent")
    print("You scored A+")
elif mark>=85:
    print("Very Good")
    print("You scored A")
elif mark>=75:
    print("Good job")
    print("You scored B+ grade")
elif mark>=65:
    print("You scured B grage")
elif mark>=55:
    print("You have secured C+ grade")
else:
    print("Keep practicing")
"""

age=int(input("Enter your age : "))
if age>=60:
    c=input("Do you have a membership card (yes/no) :")
    is_member = True if c == 'yes' else False
    if is_member:
        print("Congrats you got 30% discount")
    else:
        print("You are eligible for 10% discount")
else:
    print("Not eligible for discount")


    

