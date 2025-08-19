"""
def fun():
    name="sree" # local variable
    print(name)

fun()
"""
"""
number=23 # global variable
def fun():
    number=number+2 # cannot modify a global variable in local scope
    print(number)

fun()
"""
"""
number=23
def Add():
    global number # use global keyword to modify global variable
    number=number+2
    print(number)
"""
number=23
def Subtract(): 
    global number
    number=number+5
    print(number)

# Add()
Subtract()


    