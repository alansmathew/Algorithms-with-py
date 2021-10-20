fl=open("original_text.txt","r")
lst=list(fl.read())
fl.close()
count=0
for x in lst:
    if x=='e':
        count+=1
print("count of e is: ", count)
