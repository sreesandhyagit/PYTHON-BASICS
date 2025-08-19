txt=input("Enter a string :")  # java
c_count=dict()  # c_count={}
for x in txt: #  x=j
    if x in c_count: # if 'j' in {}
        c_count[x]=c_count[x]+1
    else:
        c_count[x]=1 # c_count{'j'=1 {"j:1}
print(c_count)
for key in c_count:
    print(key,"=",c_count[key])
