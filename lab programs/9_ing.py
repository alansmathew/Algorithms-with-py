s=input("Enter a string: ")
if (len(s)>=3):
    if(s[-3:]=='ing'):
        s=s[:-3]
        s=s+'ly'
    else:
        s=s+'ing'
print(s)
    