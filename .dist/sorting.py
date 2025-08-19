numbers=[34,1,98,4,3]
# numbers.sort()
# print(numbers)
length=len(numbers)
"""
for k in range(length):
    for j in range(length-k-1):
        if numbers[j]>numbers[j+1]:
            numbers[j],numbers[j+1]=numbers[j+1],numbers[j]
        print(numbers)
print(numbers)
"""    
for k in range(length):
    swap=False
    for j in range(length-k-1):
        if numbers[j]>numbers[j+1]:
            numbers[j],numbers[j+1]=numbers[j+1],numbers[j]
            swap=True
        print(numbers)
        if swap==False:
            break
print(numbers)