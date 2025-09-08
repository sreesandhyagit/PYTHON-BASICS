"""
class A:
    title="A"

class B(A):
    def Display(self):
        print(self.title)

obj=B()
obj.Display()
print(obj.title)
obj.title="hai"
obj.Display()

"""
"""
class A:
    def __init__(self,t):
        self.title=t

class B(A):
    def Display(self):
        print(self.title)

obj=B("Class B")
obj.Display()
print(obj.title)
obj.title="hai"
obj.Display()
"""
class A:
    def methodA(self):
        print("Hai from class A")

class B(A):
    def Display(self):
        print("Hai from class B")

obj=B()
obj.methodA()
obj.Display()
