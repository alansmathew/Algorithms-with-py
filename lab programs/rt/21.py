fl=open("Myprofile.txt","r")
f2=open("Myprofile_copy.txt","r")
lst1=fl.readlines()
lst2=f2.readlines()
fl.close()
f2.close()
lst3=lst2.copy()
i=0
while(i<len(lst3)):
    lst3[i]=lst1[i].rstrip("\n")+" "+lst2[i].rstrip("\n")+"\n"
    i+=1
f2=open("Myprofile_copy1.txt","w+")
f2.writelines(x for x in lst3)
f2.close()
print("done")