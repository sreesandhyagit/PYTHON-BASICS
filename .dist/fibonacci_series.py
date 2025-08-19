a,b=0,1
c=10
print(a,b,end=" ")
for n in range(c-2):
    t=a+b
    print(t,end=" ")
    a,b=b,t
    

