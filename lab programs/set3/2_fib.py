n=int(input("Enter a number : "))
n1=temp=0
n2=1
print("Fibonacci series : ",n1,n2,end=" ")
while (n2+n1)<n:
    temp=n2
    n2+=n1
    n1=temp
    print(n2,end=" ")
