class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    
    def add_details(self):
        with open("Student_File.txt","a") as file:
            file.write(f"{self.name}|{self.age}|{self.course}\n")
                    
    @staticmethod
    def display_details():
         with open("Student_File.txt","r") as file:
            details = file.readlines()
            print("Student Details")
            # for k, line in enumerate(details,start=1):
            #     Student =line.strip().split('|')
            #     print(f"{k}.{Student[0]} {Student[1]} {Student[2]}")
            for line in details:
                Student =line.strip().split('|')
                print("-----------------------------")
                # print("Name\t:{:>20}".format(Student[0]))
                # print(f"Age\t:{Student[1]:>20}")
                # print("Course\t:%17s" %Student[2])
                print("Name\t:{}".format(Student[0]))
                print(f"Age\t:{Student[1]}")
                print("Course\t:",Student[2])
        

# with open("Student_File.txt","w") as std_file: # Create File for one time run
#     pass

std_count = int(input("Enter the number of student: "))
for k in range(std_count):
    name = input("Enter the student name: ")
    age = int(input("Enter age:"))
    course = input("Enter course: ")
    std = Student(name, age, course)
    std.add_details()

Student.display_details()
  
   



