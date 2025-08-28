s={45,3,8,12,"Sree",7.2} #unordered, not allowed duplicates, mutable
print(s)
s.add("Kozhikode")
print("Add : ",s)
s.update(['Oneteam',67,'A'])
print(s)
s.remove('Sree')
print(s)
s.discard("A")
print(s)
s.discard(10)
s.pop()
print("After pop :",s)
print(s.pop())

set1={56,"Kochi",12,'Python'}
set2={12,"Kochi",56,'Java'}
print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))
print(set2.difference(set1))

set1={56,"Kochi",12,'Python'}
set2={12,"Kochi",56,'Java','Python'}
print(set1.issubset(set2))
print(set2.issubset(set1))



