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

class Dog(Animal):
    def sound(self):
        return "Bark"
    
class Cat(Animal):
    def sound(self):
        return "Meow"
    
d=Dog()
c=Cat()

print("Dog Sound ",d.sound())
print("Cat Sound ",c.sound())

        