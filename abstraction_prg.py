from abc import ABC,abstractmethod

# class A(ABC):
#     @abstractmethod
#     def greeting(self):
#         pass
        
# class B(A):
#     def greeting(self):
#         print("Good Evening")

# obj=B()
# obj.greeting()

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

    @abstractmethod
    def fun(self):
        pass

    def display(self):
        print("hi")

class Dog(Animal):
    def sound(self):
        return "Bark"
    
    def fun(self):
        return "fun in dog"
    
class Cat(Animal):
    def sound(self):
        self.display()
        return "Meow"
    def fun(self):
        return "fun in cat"


        
    
d=Dog()
c=Cat()

print("Dog Sound ",d.sound())
print("Cat Sound ",c.sound())
print("Dog  ",d.fun())
print("Cat  ",c.fun())

        