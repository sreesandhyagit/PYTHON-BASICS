# python is not pure object oriented

class A:
    def __init__(self):
        self.__course="Python" # private
        self._name="Priya" # protected
        self.age=18

    def display(self):
        print("Hell Developer")
        print("My course is",self.__course)

    def __displayName(self):
        print("My name is ",self._name)

    def _displayAge(self):
        print("My age is",self.age)

obj=A()
# print(obj.__course) # error
print(obj._A__course) # private data member accessed by outside
print(obj._name) # protected data member accessed by outside
print(obj.age) # public data member accessed by outside
obj.display()
obj._A__displayName()
obj._displayAge()


