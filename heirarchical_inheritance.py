# class Animal:
#     def funAnimal(self):
#         print("Class Animal")
# class Dog(Animal):
#     def funDog(self):
#         print("Class Dog")
# class Cat(Animal):
#     def funCat(self):
#         print("Class Cat")

# obj1=Animal()
# obj1.funAnimal()

# obj2=Dog()
# obj2.funAnimal()
# obj2.funDog()

# obj3=Cat()
# obj3.funAnimal()
# obj3.funCat()



# class Animal:
#     def __init__(self):
#         print("Class Animal")
# class Dog(Animal):
#     def __init__(self):
#         print("Class Dog")
#         super().__init__()
# class Cat(Animal):
#     def __init__(self):
#         print("Class Cat")
#         super().__init__()

# obj1=Animal()
# print("")
# obj2=Dog()
# print("")
# obj3=Cat()

class BaseClass:
    def __init__(self):
        self.a=10
        self.b=20
        self.c=30
        

class Child1(BaseClass):
    def DisplayChild1(self):
        print(self.a)

class Child2(BaseClass):
    def add(self):
        print(self.a+self.b+self.c)

c1=Child1()
c1.DisplayChild1()

c2=Child2()
c2.add()

c=BaseClass()
print(type(c))
print(type(c2))
print(type(c1))
n="Sreesandhya"
print(type(n))

