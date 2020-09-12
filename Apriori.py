def fun_support():
    print("\n\n----Support-----\n")
    for x in elements.copy():
        support=0
        for y in ls:
            if x in y: 
                support+=1
        print('%s\t' %x,'%d' %support,'%d' %len(ls),'%d'%int((support/len(ls))*100),'%\t',end='')
        if (support/len(ls))*100<minsup:
            print('❌')
            elements.pop(elements.index(x))
        else:print('✅')
    print('\nSelected elements after sorting support : ',', '.join(elements))

def func_confidence(elements):
    print('\n\n\n----confidence-----\n')
    confidance=[]
    elcpy=elements.copy()
    while len(elcpy)>0:
        for j in [item for item in elcpy if item not in elcpy[0]]:
            count=0;sup='❌'
            for k in ls:
                if ((elcpy[0] in k) and (j in k)):count+=1
            if((count/len(ls)*100)>=minsup):
                sup='✅'
                if(elcpy[0] not in confidance):confidance.append(elcpy[0])
                if(j not in confidance): confidance.append(j)
            print('%s'%elcpy[0],'%s\t\t'%j,'= %s'%j,'%s\t '%elcpy[0],'%d'%count,'%d'%len(ls),'%d'%int(count/len(ls)*100),'%s'%sup)
        elcpy.pop(0)
    print('\nSelected elements after sorting confidence : ',', '.join(confidance),)
    return confidance

def func_confidence_c3(confidance):
    print('\n----c3----\n')
    poss_combination=[]
    retuening_elements=[]
    for q in confidance:
        for w in [item for item in confidance if item != q]:
            for e in [item for item in confidance if (q != w) and (w !=item) and (q != item) ]:
                items = q +' '+ w +' '+ e
                items=list(items.split(' '))
                count=0
                for x in ls:
                    if e in x and w in x and q in x:
                        count+=1
                flag=True
                if len(poss_combination)==0:
                    poss_combination.append(items)
                    if(int(count/len(ls)*100)>=minsup):
                        retuening_elements.append(q); retuening_elements.append(w); retuening_elements.append(e)
                    print('%s'%q,'%s'%w,'%s\t\t'%e,'%d'%count,'%d'%len(ls),'%d'%int(count/len(ls)*100),'%\t', (int(count/len(ls)*100)>=minsup) and '✅' or '❌')
                    break
                else:
                    for a in items:
                        for b in [item for item in items if item !=a]:
                            for c in [item for item in items if (item != a) and (item != b)]:
                                inner_item = a +' '+ b +' '+ c
                                inner_item = list(inner_item.split(' '))
                                if inner_item in poss_combination:
                                    flag=False
                    if flag == True :
                        poss_combination.append(items)
                        print('%s'%q,'%s'%w,'%s\t\t'%e,'%d'%count,'%d'%len(ls),'%d'%int(count/len(ls)*100),'%\t',(int(count/len(ls)*100)>=minsup) and '✅' or '❌')
                        if (int(count/len(ls)*100)>=minsup):
                            if q not in retuening_elements:
                                retuening_elements.append(q)
                            if w not in retuening_elements:
                                retuening_elements.append(w)
                            if e not in retuening_elements:
                                retuening_elements.append(e)
    print('\nSelected elements after sorting confidence : ',', '.join(retuening_elements))
    return retuening_elements


# ls=[]
# for x in range(0,int(input('No of T : '))):
#     el=[]
#     for j in range(0,int(input('No of elements : '))):
#         el.append(input("Enter element : "))
#     ls.append(el)
# print(ls)
ls=[['I1', 'I2', 'I5'], ['I2', 'I4'], ['I2', 'I3'], ['I1', 'I2', 'I4'], ['I1', 'I3'], ['I2', 'I3'], ['I1', 'I3'], ['I1', 'I2', 'I3', 'I5'], ['I1', 'I2', 'I3']]
# ls=[['beef', 'chicken', 'milk'], ['beef', 'cheese'], ['cheese', 'boots'], ['beef', 'chicken', 'cheese'], ['beef', 'chicken', 'clothes', 'cheese', 'milk'], ['chicken', 'clothes', 'milk'], ['chicken', 'milk', 'clothes']]
# minsup = int(input("minsup = "))
# minconf = int(input("minconf = "))
minsup = 22
minconf = 70
elements =[]
for x in ls:
    for j in x:
        if str(j) not in elements :
            elements.append(str(j))
print('\n\n',elements)

fun_support()
confidance = func_confidence(elements)
c3 = func_confidence_c3(confidance)




poss_combination_conf=[]
for q in c3:
    for w in [item for item in c3 if item != q]:
        for e in [item for item in c3 if (q != w) and (w !=item) and (q != item) ]:
            items = q +' '+ w +' '+ e
            if list(items.split(' ')) not in poss_combination_conf:
                if len(poss_combination_conf)>0:
                    flag=True
                    for r in poss_combination_conf:
                        if (r[0]==q) and (r[1]==e) and (r[2]==w):
                            flag = False
                    if flag == True :
                        poss_combination_conf.append(list(items.split(' ')))
                else: poss_combination_conf.append(list(items.split(' ')))
            
valid_comp=[]
print("\n----Final confidence----\n")
for r in poss_combination_conf:
    numerator,deno=0,0
    for t in ls:
        if (r[0] in t) and (r[1] in t) and (r[2] in t):numerator+=1
        if r[0] in t: deno+=1
    if((numerator/deno)*100)>=minconf: 
        comp=r[0]+' '+ '->'+' '+r[1]+' '+r[2]
        valid_comp.append(list(comp.split(' ')))
    print('%s'%r[0],'%s '%'->','%s'%', '.join(r[1:]),'\t%d'%numerator,'%d'%deno,'%.0f\t'%((numerator/deno)*100),(((numerator/deno)*100)>=minconf) and '✅' or '❌')

for r in poss_combination_conf:
    numerator,deno=0,0
    for t in ls:
        if (r[0] in t) and (r[1] in t) and (r[2] in t):numerator+=1
        if r[2] in t: deno+=1
    if((numerator/deno)*100)>=minconf:
        comp=r[1]+' '+r[2]+' '+'->'+' '+r[0]
        valid_comp.append(list(comp.split(' ')))
    print('%s'%', '.join(r[1:]),'%s '%'->','%s'%r[0],' \t%d'%numerator,'%d'%deno,'%.0f\t'%((numerator/deno)*100),(((numerator/deno)*100)>=minconf) and '✅' or '❌')

print("\n-----Final association-----\n")
if len(valid_comp):
    for i in valid_comp:
        print(' '.join(i))
else:print('nill')