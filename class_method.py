# class MyClass:
#     class_variable = "I am a class variable"

#     @classmethod
#     def print_class_variable(cls):
#         print(cls.class_variable)

#     @classmethod
#     def create_instance_with_message(cls, message):
#         instance = cls()
#         instance.message = message
#         return instance

# # Accessing a class method
# MyClass.print_class_variable()

# # Using a class method as an alternative constructor
# obj = MyClass.create_instance_with_message("Hello from an alternative constructor!")
# print(obj.message)

# class Student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     @classmethod
#     def new_student(cls,name,age):
#         return cls(name,age)
    
# std=Student("Jacob",30)
# print(std)
# std2=Student.new_student("Sreesandhya",30)

# print(std2.name)

# Python program to demonstrate
# use of class method and static method.
from datetime import date


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # a class method to create a Person object by birth year.
    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year - year)

    # a static method to check if a Person is adult or not.
    @staticmethod
    def isAdult(age):
        return age > 18


person1 = Person('mayank', 21)
person2 = Person.fromBirthYear('mayank', 1996)

print(person1.age)
print(person2.age)

# print the result
print(Person.isAdult(22))