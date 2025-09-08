"""
class Laptop:
    def __init__(self,model):
        print("Hello")
        print(model)
       
lp=Laptop()
lp1=Laptop("Azuz Tuf")
lp2=Laptop("Dell")
# lp2=Laptop() # Error
"""
"""
class Laptop:
    def __init__(self,m):
        self.model=m

    def display(self):
        print("Model : ",self.model)


lp1=Laptop("Azuz Tuf")
lp2=Laptop("Dell")

lp1.display()
lp2.display()
"""
# self is not a keyword.. it is used for object reference of function in class
class Students:
    def __init__(self,n,a): # self is object reference of constructor & n and a are parameters
        self.name=n
        self.age=a

    def display(self): # self is object reference of display
        self.place="Kochi"
        print(f"Your name is {self.name} and you are {self.age} years old")

    def fun():
        print("Hai im no self")


# st1=Students("Devika",23)
# st2=Students("Anupama",21)

# st1.display()
# st2.display()

obj=Students("Priya",20)
print(obj.name)
# st1.display()
# print(st1.place)

Students.fun()
# Students.display("Rinu",21)# this will make error
stud1=Students("Karan",22)
stud1.display()



