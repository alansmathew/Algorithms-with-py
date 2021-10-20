fl=open("test20.txt","r")
lst=fl.read()
fl.close()
lst=lst.split()
for x in lst:
    print(x.capitalize(),end=" ")