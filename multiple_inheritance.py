# class A:
#     def methodA(self):
#         self.a=10
# class B:
#     def methodB(self):
#         self.b=20
# class C(A,B):
#     def result(self):
#         print(self.a+self.b)

# obj1=C()
# obj1.methodA()
# obj1.methodB()
# obj1.result()

# class A:
#     def methodA(self,av):
#         self.a=av
# class B:
#     def methodB(self,bv):
#         self.b=bv
# class C(A,B):
#     def result(self):
#         print(self.a+self.b)

# obj1=C()
# obj1.methodA(10)
# obj1.methodB(20)
# obj1.result()


# class A:
#     def __init__(self,av,n):
#         self.a=av
#         B.__init__(self,n)
# class B:
#     def __init__(self,bv):
#         self.b=bv
# class C(A,B):
#     def result(self):
#         print(self.a+self.b)

# obj1=C(10,20)
# obj1.result()


class A:
    def __init__(self):
        print("Class A")
        B.__init__(self)
class B:
    def __init__(self):
        print("Class B")
class C(A,B):
    def __init__(self):
        print("Class C")
        super().__init__()

obj=C()

class A:
    def __init__(self,av,n):
        self.a=av
        B.__init__(self,n)
class B:
    def __init__(self,bv):
        self.b=bv
class C(A,B):
    def __init__(self,r,s):
        super().__init__(r,s)
        print(self.a+self.b)

obj1=C(10,20)
