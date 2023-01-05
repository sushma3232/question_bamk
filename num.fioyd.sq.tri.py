

n=4
p=1
for i in range(n):
    for j in range(i+1):
        print(p**2,end=" ")
        p=p+1
    print()
    
    
i=0
p=1
while i<=3:
    j=0
    while j<=i:
        print(p**2,end=" ")
        j=j+1
        p=p+1
    print()
    i=i+1
        