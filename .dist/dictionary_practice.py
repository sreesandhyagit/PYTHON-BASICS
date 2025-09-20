

student={"name":'Aleena',"age":27,6:'Python'}
print(student["name"])
# print(student['place'])
print(student.get('name'))
print(student.get('place'))
print(student.get('place',"Not Found!"))
student['place']="Kozhikode"
print(student)
student['age']=30
print(student)
student.update({'place':"Kochi"})
print(student)
print(student.pop(6))
print(student)

d=student.popitem()
print("Dictionary after pop item :",student)
print("Deleted item is :",d)

print(student.items())

for s in student:
    print(s,student[s])

for k,v in student.items():
    print(k,v)


l=('RAM','model','storage',7)
laptop=dict.fromkeys(l)
print(laptop)

l=('RAM','model','storage',7)
k="unknown"
laptop=dict.fromkeys(l,k)
print(laptop)


l=('RAM','model','storage',7)
k=('4GB',"Dell","512GB","Python")
laptop=dict.fromkeys(l,k)
print(laptop)





