prime=True
num=int(input("Enter a number"))
if num>1:
    for r in range(2,(num//2)+1):
        if num%r==0:
            prime=False
            break
    if prime:
        print("It is prime")
    else:
        print("It is not prime")
else:
    print("It is not prime...it must be greater than 1")
