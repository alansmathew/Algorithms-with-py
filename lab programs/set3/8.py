def factor(n,i):
    if i==n:
        return
    if(n%i==0):
        print(i,end=" ")
    factor(n,i+1)
factor(int(input("Enter a number : ")),1)
