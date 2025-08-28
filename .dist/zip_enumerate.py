
l=('RAM','model','storage',7)
k=('4GB',"Dell","512GB","Python")
print(list(zip(l,k)))

l=('RAM','model','storage',7)
k=('4GB',"Dell","512GB","Python")
for k,v in zip(l,k):
    print(k,v)
    
l=('RAM','model','storage',7)
k=('4GB',"Dell","512GB","Python")
j=('Azus','Medium','SSD')
for k,v,a in zip(l,k,j):
    print(k,v,a)