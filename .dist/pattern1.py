"""
for a in range(1,6):
    print(" *"*a)

for n in range(1,6):
    print(n)
print("welcome")

for n in range(1,6):
    print(n,end="")
print("hai")

print("\n")
for n in range(1,6):
    print(n,end=" ")
print("hi")
print("hello")


for n in range(1,6):
    for k in range(1,n+1):
        print(k,end=" ")
    print("")

 
for n in range(5,0,-1):
    print("*"*n)"""
    
"""for row in range(1,6):
    for sp in range(5-row):
        print(" ",end="")
    for column in range(row):
        print("*",end=" ")
    print("")"""

"""star=1
for row in range(1,6):
    for sp in range(5-row):
        print(" ",end="")
    for column in range(star):
        print("*",end="")
    star+=2
    print("")

for row in range(1,6):
    for sp in range(row):
        print(" ",end="")
    for column in range(5-row):
        print("*",end=" ")
    print("")"""

"""star=15
for row in range(1,9):
    for sp in range(row):
        print(" "*3,end=" ")
    for column in range(star):
        print(" * ",end=" ")
    print("")
    star-=2
"""
"""
star=15
for row in range(1,9):
    for sp in range(row):
        print(" ",end="")
    for column in range(star):
        print("*",end="")
    print("")
    star-=2
    """
"""text="Sreesandhya"
t=len(text)
for row in range(1,12):
    # for sp in range(row):
        # print(" ",end="")
    for column in range(t):
        print(text[column]," ",end="")
    print("")
    t-=1
    """
"""
for row in range(1,6):
    print(row,end=" ")
    i=4
    n=row+i
    for column in range(1,row):
        print(n,end=" ")
        i=i-1
        n=n+i
    print("")
"""
for row in range(1,6):
    num=row
    counter=4
    for column in range(row):
        print(num,end=" ")
        num=num+counter
        counter-=1
    print("")
    

"""
no_rows=int(input("How many rows you want to print pattern :"))
for row in range(1,no_rows+1):
    print(row,end="  ")
    i=no_rows-1
    n=row+i
    for column in range(1,row):
        print(n,end="  ")
        i=i-1
        n=n+i
    print("")

"""
