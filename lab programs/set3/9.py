def add(a,b):
    return(a+b)
def Dif(a,b):
    return(a-b)
def pro(a,b):
    return(a*b)
def div(a,b):
    return(a/b)
op=int(input("1)Add\n2)Difference\n3)Product\n4)Divide\nEnter your choice : ")) 
a,b=int(input("Enter two numbers : ")),int(input())
d={1:add(a,b),2:Dif(a,b),3:pro(a,b),4:div(a,b)}
print("Ans=",d.get(op))
