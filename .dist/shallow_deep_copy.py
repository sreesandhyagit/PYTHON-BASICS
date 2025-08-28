import copy

l=[12,7,'Sree',9] #immutable
l2=copy.copy(l)
print(l)
print(l2)

print("-----------------------------------------------")

l=[12,7,'Sree',9] #immutable
l2=copy.deepcopy(l)
print(l)
print(l2)

print("-----------------------------------------------")

lst1=[[1,2.3],["Rani",45]]
lst2=copy.copy(lst1)
lst2[0][1]=10.7
print(lst1)
print(lst2)

print("-----------------------------------------------")

lst1=[[1,2.3],["Rani",45]]
lst2=copy.deepcopy(lst1)
lst2[0][1]=10.7
print(lst1)
print(lst2)

print("-----------------------------------------------")

k=[[12,5],['Ebin',9]]
j=k
j[1][0]='Rohit'
print(k)

print("-----------------------------------------------")
k=[[12,5],['Ebin',9]]
j=copy.deepcopy(k)
j[1][0]='Rohit'
print(k)
print(j)






