# built-in methods of list

my_list=['Python',12,7.2]

my_list.append(34)
print(my_list)

# my_list.append([45,23,4])
# print(my_list)

my_list.extend([1,12,23,5,67,9,10])
print(my_list)

my_list.remove(23)
print("After remove: ",my_list)

my_list.pop(2)
print("After pop :",my_list)

my_list.pop()
print("After empty pop ",my_list)

print(my_list.remove("Python"))
print(my_list)
print(my_list.pop(0))

my_list.sort()
print("Sorted list ascending ",my_list)
my_list.sort(reverse=True)
print("Sorted list descending ",my_list)

my_list.insert(3,'Python')
print("After insert ",my_list)
my_list.insert(3,'Python')
print("After insert ",my_list)

print(my_list.count('Python'))
print(my_list.index(9))
print(my_list.index('Python'))

my_list.reverse()
print(my_list)