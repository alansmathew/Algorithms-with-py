def Asterisks(n):
        if n >75:
                for i in range(0,75):
                        print("*" ,end=" ")
        else:
                for i in range(0,n):
                        print("*" ,end=" ")
Asterisks(int(input("Enter a number : ")))
