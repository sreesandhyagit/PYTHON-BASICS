n=int(input("Enter a number"))
fact=1
for k in range(1,n+1):
    fact=fact*k
print(f"factorial of {n} is {fact}")