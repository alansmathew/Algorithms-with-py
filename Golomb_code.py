import math
n=9
m=10
q=(n//m)+1
print("q = ",q)
x=1;flag=False
while x<=m:
    if x==m:flag=True 
    x=2*x
if flag:
    print(m," is the power of 2")
else:
    print(m," is not the power of 2")
    log=int(math.log(m,2))
    print("log2(%d)="%m,log)
    fs_base=2**(log+1)-m
    print("2 ^ log2(%d) - M = "%m,fs_base)
    poss_rem=[x for x in range(0,n%m+1)]
    print("possible reminders ",poss_rem)
    print("%d seq = "%log,poss_rem[:fs_base])
    print("%d seq = "%(log+1),poss_rem[fs_base:])
    r=n%m
    print("r =",r)