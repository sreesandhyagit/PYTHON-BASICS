def loginRequired(fun): # Decorator function definition
    def wrapper(n,status):
        if status:
            fun(n,status)
        else:
            print("Invalid User")
    return wrapper
"""
def Dashboard(name,is_authenticated):
    print("Welcome",name)

# loginRequired(Dashboard('Sree',False))

k=loginRequired(Dashboard)
print(k)
k('Sreemol',False)

"""

@loginRequired # Decorator
def Dashboard(name,is_authenticated):
    print("Welcome",name)

Dashboard("Sreesandhya",True)