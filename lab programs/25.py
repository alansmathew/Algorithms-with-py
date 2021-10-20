s1=list(input(" Enter 1st string: "))
s2=list(input(" Enter 2nd string: "))
print(" not common items are : " ,end=" " )
i=0
while i<len(s1):
    if s1[i] not in s2:
        print(s1[i], end=" ")
    i+=1
j=0
while j<len(s2):
    if s2[j] not in s1:
        print(s2[j], end=" ")
    j+=1
