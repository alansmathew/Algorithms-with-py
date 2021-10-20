def maximum(lst1):
    return(max(lst1))
lst=[]
lst.extend(int(input("Enter values: ")) for x in range(int(input("Enter a limit : "))))
print("Maximum of ",lst," is ",maximum(lst))

