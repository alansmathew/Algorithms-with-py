fl=open("Myprofile.txt","r")
lst=(fl.readlines())
fl.close()
fl=open("Myprofile_copy.txt","w+")
fl.writelines(str(x) for x in lst)
fl.close()
print("done")