s=0
for i in range (4):
    for k in range(4,i,-1):
        print(end=" ")
    for j in range(0,i+1):
        s+=1
        print(s,end=" ")

    print()
