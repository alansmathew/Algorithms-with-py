alpha=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
key='monarchy'
ls=list(key)
for x in alpha:
    if x not in ls:ls.append(x)

metrix=[]
for i in range(0,25,5):
    temp=[]
    for x in range(i,i+5):
        temp.append(ls[x])
    metrix.append(temp)
# print(metrix)

string="balloon"
temp=list([x for x in list(string) if x!=" "])
pair=[]
for x in range(0,len(temp),2):
    temp1=[]
    if len(temp)-x < 2: pair.append(list(temp[x]));break
    for x in range(x,x+2):
        temp1.append(temp[x])
    pair.append(temp1)
print(pair)