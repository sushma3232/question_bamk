


n=5
for i in range(n):
    for j in range(i+1):
        if j%2!=0:
            print("*",end=" ")
        else:
            print(i+1,end=" ")
    print()
    
    
i=0
while i<5:
    j=0
    while j<=i:
        if j%2!=0:
            print("*",end=" ")
        else:
            print(i+1,end=" ")
        j=j+1
    print()
    i=i+1