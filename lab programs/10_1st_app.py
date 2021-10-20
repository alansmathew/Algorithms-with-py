string=input("Enter string : ")
lst=string.split()
if 'not' in lst and 'poor' in lst:
    if lst.index('not') < lst.index('poor'):
        i=lst.index('not')
        j=lst.index('poor')
        while i <=j:
            lst.pop(i)
            j-=1
        lst.insert(i,'good')
newstring=" ".join(str(x) for x in lst)
print(newstring)