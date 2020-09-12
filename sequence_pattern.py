ls=[[[30],[90]],[[10,20],[30],[10,40,60,70]],[[30,50,70,80]],[[30],[30,40,70,80],[90]],[[90]]]
elements=[]
# ls=[ [[1,2,4],[2,3],[5]] , [[1,2],[2,3,4]] , [[1,2],[2,3,4],[2,4,5]], [[2],[3,4],[4,5]] , [[1,3],[2,4,5]] ]
support=25
for x in ls:
    for y in x:
        for z in y: 
            if z not in elements:
                elements.append(z)
elements.sort()
# print(elements)
for a in elements.copy():
    count=0
    for x in ls:
        for y in x:
            if a in y:
                count += 1
                break
    if (count/len(ls))*100 <= support:
        elements.pop(elements.index(a))
print(elements)


# ------------2nd sequence --------------
for x in elements:
    for y in [item for item in elements.copy() if item != x]:
        # print(x,y)
        count=0
        for a in ls:
            for b in a:
                if x in b:
                    for c in a: 
                        if a.index(b) < a.index(c) and y in c:count+=1
        if (count/len(ls))*100 >= support:
            print('{%d},{%d}'%(x,y))
        
        count2=0
        for a in ls:
            for b in a:
                if (x in b) and (y in b) and (b.index(x)<b.index(y)):
                    count2+=1
        if (count2/len(ls))*100 >= support:
            print( '{%d %d}'%(x,y) )