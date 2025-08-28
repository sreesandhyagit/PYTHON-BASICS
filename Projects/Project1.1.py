# Student Report Card Management System
"""
Create a program that allows users to manage student record including roll numbers, names, marks & grades.
The program can accept inputs, calculate grades, store data and display reports
Input :Roll Number, Name & marks for three subjects
Calculate : Total mark, Average mark and find grade based on average
Allow entry for multiple students
Display student report

"""
from functools import reduce

print("Student Report Card Management System")
record={}
pos=1

while True:
    print("STUDENT REPORT CARD MANAGEMENT SYSTEM")
    print("1. Add Student\n2. View Report\n3. Update Student\n4. Delete Student\n5. Show All Students\n6. Exit")
    choice=int(input("Enter your choice :"))
    match choice:
        case 1:
            while True:
                print("ADD STUDENT")
                roll_no=int(input("Enter Roll Number : "))
                name=input("Enter name :")
                print("Enter the mark of subjects : ")
                maths=int(input("Maths : "))
                eng=int(input("English : "))
                sci=int(input("Science : "))

                marks={"Maths":maths,"English":eng,"Sciecnce":sci}
              
                sum=reduce(lambda a,b:a+b,[maths,eng,sci])
                avg=round((float(sum/3)),2)
                per=round(float((sum*100)/150),2)

                if per>=90:
                    grade="A"
                elif avg>=80:
                    grade="B"
                elif avg>=70:
                    grade="C"
                elif avg>=60:
                    grade="D"
                else:
                    grade="E"

                student={}
                student[roll_no]={'Name':name,'Marks':marks,'Total':sum,'Average':avg,'Percentage':per,'Grade':grade}
              
                record[pos]=student
                pos+=1

                repeat=input("Do you want to continue (yes/no) : ")
                if repeat=="yes":
                    continue
                else:
                    break

            print()
            print("STUDENTS REPORT\n")
            for k in record:
                print(record[k]['Name'],"\t",record[k]['Average'],"\t",record[k]['Grade'])




