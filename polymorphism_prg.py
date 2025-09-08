class A:
    def greeting(self):
        print("Good Evening")

class B(A):
   def greeting(self):
        print("Hello from class B")


obj=B()
obj.greeting()
