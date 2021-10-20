def Getdailytemps():
    lst=["monday","tuesday","wednessday","thursday","friday","saturday","sunday"]
    dic={}
    for key in lst:
        print("Enter the avg temprature of ",key," : ",end=" ")
        value=int(input())
        dic.update({key:value})
    return dic
print(Getdailytemps())
