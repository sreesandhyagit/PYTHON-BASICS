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
i=1
while True:
    student={}
    roll_no=int(input("Enter Roll Number : "))
    name=input("Enter name :")
    print("Enter the mark of 3 subjects :")
    marks=[]
    for k in range(3):
        m=int(input("Enter mark :"))
        marks=marks+[m]
    sum=reduce(lambda a,b:a+b,marks)
    avg=round((float(sum/3)),2)
    if avg>=40:
        grade="A"
    elif avg>=30:
        grade="B"
    elif avg>=20:
        grade="C"
    else:
        grade="D"
   
    student["Roll No"]=roll_no
    student['Name']=name
    student['Marks']=marks
    student['Total']=sum
    student['Average']=avg
    student['Grade']=grade

    record[i]=student
    i+=1
    repeat=input("Do you want to continue (yes/no) : ")
    if repeat=="no":
        break
print()
print("STUDENTS REPORT\n")
for k in record:
    print(record[k]['Name'],"\t",record[k]['Average'],"\t",record[k]['Grade'])
    print(record)




