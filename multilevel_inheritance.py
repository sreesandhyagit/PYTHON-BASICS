# class Vehicle:
#     def funVehicle(self):
#         print("Class Vehicle")
# class Car(Vehicle):
#     def funCar(self):
#         print("Class Car")
# class Duster(Car):
#     def funDuster(self):
#         print("Class Duster")

# obj1=Vehicle()
# obj1.funVehicle()

# obj2=Car()
# obj2.funVehicle()
# obj2.funCar()

# obj3=Duster()
# obj3.funVehicle()
# obj3.funCar()
# obj3.funDuster()

class Vehicle:
    def __init__(self):
        print("Class Vehicle")
class Car(Vehicle):
    def __init__(self):
        print("Class Car")
        super().__init__()
class Duster(Car):
    def __init__(self):
        print("Class Duster")
        super().__init__()


obj1=Vehicle()
print("")
obj2=Car()
print("")
obj3=Duster()
