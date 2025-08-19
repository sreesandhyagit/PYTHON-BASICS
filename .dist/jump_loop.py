"""
for num in range(1,11):
    if num==5:
        break;
    print(num,end=" ")
print("\nloop executed")

print("")
for num in range(1,11):
    if num==5 or num==8:
        continue;
    print(num,end=" ")
    """
num=1
while num<=5:
    if num==3:
        break
    print(num,end=" ")
    num=num+1

print("")

num=1
while num<=5:
    if num==3:
        num=num+1
        continue
    print(num,end=" ")
    num=num+1

