list1=['a','b','c','d','e','f','g']
print("alternatives starting with 'a'= ",[list1[x] for x in range(0,len(list1),2)])
print("alternatives starting with 'b'= ",[list1[i] for i in range(1,len(list1),2)])
list1.sort()
print(list1)
list1.sort(reverse=True)
print(list1)
list2=['ann','seri']
list2.append(list1)
print(list2)
list2.extend(list1)
print(list2)
for i in list1:
    print(i, end=" ")
print()
for x in list1:
    print(x,list1.index(x))