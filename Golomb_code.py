import math
# n=15
# m=10
# q=(n//m)+1
# print("q = ",q)
# x=1;flag=False
# while x<=m:
#     if x==m:flag=True 
#     x=2*x
# if flag:
#     print(m," is the power of 2")
# else:
#     print(m," is not the power of 2")
#     log=int(math.log(m,2))
#     print("log2(%d)="%m,log)
#     fs_base=2**(log+1)-m
#     print("2 ^ log2(%d) - M = "%m,fs_base)
#     poss_rem=[x for x in range(0,n%m+1)]
#     print("possible reminders ",poss_rem)
#     print("%d seq = "%log,poss_rem[:fs_base])
#     print("%d seq = "%(log+1),poss_rem[fs_base:])
#     r=n%m
#     print("r =",r)

#decoading 
bin="0000110"
b=3
count=0
for x in list(bin):
    if int(x)==0:count+=1
    else:break
print("q = ",count," u(q+1)= ",count+1)
i=int(math.log(b,2))
print("i = log2(%d) = "%b,i)
d=2**(i+1)-b
print("d = 2 ^ (i+1) - b = 2 ^ (%d+1) - b ="%i ,d)
print("retriving next %d bits"%i)
binar="".join(list(bin)[count+1:i+count+1])
ls=list(binar)[::-1]
dec=0
for x in range(0,len(ls)):
    dec+=(2**(x))*int(ls[x])
print("r = ",binar," = > ",dec)
if dec >= d:
    binar="".join(list(bin)[count+1:i+count+2])
    ls1=list(binar)[::-1]
    dec=0
    for x in range(0,len(ls1)):
        dec+=(2**(x))*int(ls1[x])
    print("appending one more bit to r =",binar," => ",dec)
    print("r = %d"%dec," - %d"%d," = ",dec-d )
    print("x= qb + r = ",count*b+(dec-d))
else:
    print("have to do ")