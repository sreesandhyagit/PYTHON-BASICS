n=int(input("Enter an integer number :"))
if n%2==1:
    print("Weired")
else:
    if n>=2 and n<=5:
        print("Not Weired")
    elif n>=6 and n<=20:
        print("Weired")
    elif n>20:
        print("Not Weired")