# class A:
#     title="Class A"
#     def Greetings(self):
#         print("Greetings from class A")

# class B(A):
#     def showTitle(self):
#         print(self.title)

# obj=B()
# print(obj.title)
# obj.Greetings()
# obj.showTitle()
"""
class A:   
    def __init__(self):
        title="Class A"
        print("Greetings from class A")

class B(A):
    def __init__(self):
        print(self.title)

obj=B()
"""


# class A:   
#     def __init__(self):
#         print("Greetings from class A")

# class B(A):
#     def __init__(self):
#         print("Greetings from class B")
#         super().__init__()

# obj=B()


class A:   
    def __init__(self):
        self.title="Class A"
        print("Greetings from class A")

class B(A):
    def __init__(self):
        print("Greetings from class B")
        super().__init__()
        print(self.title)

obj=B()