# class Student:
#     @staticmethod
#     def validate(mark):
#         if mark>50:
#             return "pass"
#         else:
#             return "fail"
        
#     def __init__(self,m):
#         self.mark=m

#     def result(self):
#         print(Student.validate(self.mark))
#         print(self.validate(self.mark))


# st1=Student(100)
# st1.result()
# print(Student.validate(99))
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b

# Accessing a static method
result_add = MathUtils.add(5, 3)
print(f"Addition: {result_add}")

result_multiply = MathUtils.multiply(4, 2)
print(f"Multiplication: {result_multiply}")