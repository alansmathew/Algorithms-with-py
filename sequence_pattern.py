# ls=[[[30],[90]],[[10,20],[30],[10,40,60,70]],[[30,50,70,80]],[[30],[30,40,70,80],[90]],[[90]]]
elements=[]
ls=[[["a"],["abc"],["ac"],["d"],["cf"]],[["ad"],["c"],["bc"],["ae"]],[["ef"],["ab"],["df"],["cb"]],[["eg"],["af"],["cbc"]]]
# ls=[ [[1,2,4],[2,3],[5]] , [[1,2],[2,3,4]] , [[1,2],[2,3,4],[2,4,5]], [[2],[3,4],[4,5]] , [[1,3],[2,4,5]] ]
support=2
for x in ls:
    for y in x:
        for z in y: 
            if z not in elements:
                elements.append(z)
elements.sort()
# print(elements)
print('1st sequence ')
for a in elements.copy():
    count=0
    for x in ls:
        for y in x:
            if a in y:
                count += 1
                break
    print('<{%d}>\t %d\t %d\t %d\t %s'%(a,count,len(ls),int((count/len(ls))*100),(int(count/len(ls)*100)>=support) and '✅' or '❌'))
    if (count/len(ls))*100 <= support:
        elements.pop(elements.index(a))

print(elements,'\n\n')


# ------------2nd sequence --------------
necc_1sequence=[]
necc_2sequence=[]
temp_necc_1sequence = []
ans=[]
print('2nd sequence\n')
for x in elements:
    for y in [item for item in elements if item != x]:
        count=0
        for a in ls:
            for b in a:
                if x in b:
                    for c in a: 
                        if a.index(b) < a.index(c) and y in c:count+=1
        print('<{%d},{%d}>\t%d\t%d\t%d\t%s'%(x,y,count,len(ls),int(count/len(ls)*100),(int(count/len(ls)*100)>=support) and '✅' or '❌'))
        if (count/len(ls))*100 >= support:
            # print('<{%d},{%d}>'%(x,y))
            item='<{%d},{%d}>'%(x,y)
            ans.append(item)

            temp_necc_1sequence.append([x,y])
            if x not in necc_1sequence: necc_1sequence.append(x)
            if y not in necc_1sequence: necc_1sequence.append(y)
        
        count2=0
        for a in ls:
            for b in a:
                if (x in b) and (y in b) and (b.index(x)<b.index(y)):
                    count2+=1
        print('<{%d,%d}>\t%d\t%d\t%d\t%s'%(x,y,count2,len(ls),int(count2/len(ls)*100),(int(count2/len(ls)*100)>=support) and '✅' or '❌'))
        if (count2/len(ls))*100 >= support:
            item='<{%d %d}>'%(x,y)
            ans.append(item)
            # print( '<{%d %d}>'%(x,y) )
            necc_2sequence.append([x,y])


print("\nanswer=",end=' ')
for x in ans:
    print(x,end=', ')   

print()        
# necc_ [[30, 70], [30, 80], [40, 70], [70, 80]]

# ---- 3rd sequences ------ 

print('\n\n3rd sequence\n')
ans3=[]
for x in necc_1sequence:
    for y in [item for item in necc_1sequence if item != x]:
        for z in necc_2sequence:
            if z[0] == y:
                count3,count4=0,0
                for c in ls:
                    for v in c:
                        if x in v :
                            if (z[0] in v) and (z[1] in v ) and (v.index(x) < v.index(z[0]) < v.index(z[1])): count4+=1
                            for b in c:
                                if (c.index(v)<c.index(b)) and (z[0] in b) and (z[1] in b) and (b.index(z[0])<b.index(z[1])): count3+=1
                # print('<{%d}{%d,%d}>\t%d\t%d\t%d\t%s'%(x,z[0],z[1],count3,len(ls),int(count3/len(ls)*100),(int(count3/len(ls)*100)>=support) and '✅' or '❌' ))
                # print('<{%d,%d,%d}>\t%d\t%d\t%d\t%s'%(x,z[0],z[1],count4,len(ls),int(count4/len(ls)*100),(int(count4/len(ls)*100)>=support) and '✅' or '❌' ))
                if (count3/len(ls))*100 >= support:
                    item='<{%d}{%d,%d}>'%(x,z[0],z[1])
                    ans3.append(item)
                    # print('<{%d}{%d,%d}>, '%(x,z[0],z[1]), end=' ')
                if (count4/len(ls))*100 >= support:
                    item='<{%d,%d,%d}>'%(x,z[0],z[1])
                    ans3.append(item)
                    # print('<{%d,%d,%d}>'%(x,z[0],z[1]), end=' ')

print("\nanswer=",end=' ')
for x in ans3:
    print(x,end=', ')
print()  


# # [[10,20],[30],[10,40,60,70]]
# for x in necc_2sequence:
#     for a in temp_necc_1sequence:
#         count5=0
#         if x[1]==a[0]:
#             for b in ls:
#                 for c in b:
#                     if (x[0] in c) and (x[1] in c ):
#                         item=[i for i in b if i != c]
#                         # print(item)
#                         for d in item:
#                             if (a[1] in d) and  ( b.index(d) < d.index(a[1]) ): count5+=1
#         if (count5/len(ls))*100 >= support:
#             print('<{%d,%d}{%d}>   %d, '%(x[0],x[1],a[1],count5), end=' ')