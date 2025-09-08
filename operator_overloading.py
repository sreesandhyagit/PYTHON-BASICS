# a=2
# b=3
# print(a+b)
# a="python"
# b="class"
# print(a+b)


# class A:
#     def __init__(self,varA,varB):
#         self.a=varA
#         self.b=varB

# obj1=A(21,20)
# obj2=A(3,8)
# print(obj1+obj2)

# magic methods for operator overloading

class A:
    def __init__(self,varA,varB):
        self.a=varA
        self.b=varB
    
    def __add__(self,other):
        return self.a+other.a,self.b+other.b
    
    def __sub__(self,other):
        return self.a-other.a,self.b-other.b
    
       
    
obj1=A(21,20)
obj2=A(3,8)
print(obj1+obj2)
print(obj1-obj2)

