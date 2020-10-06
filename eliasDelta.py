import math
def encoading(num):
    s=""
    for x in range(num-1):
        s+=str(0)
    return s+str(1)
def binary(number):
    ls=[]
    def bin(num):
        if num>0:
            bin(num//2)
            ls.append(num%2)
    bin(number)        
    return int("".join([str(x) for x in ls]))

# number=int(input("Enter encoding number: "))
number=13
first_val=int(math.log(number,2))+1
print("1+log2(%d) ="%number,first_val)
second_val=int(math.log(first_val,2))+1
print("1+log2(%d) ="%first_val,second_val)
unery=encoading(second_val) ; bin= binary(first_val)
print("unery of %d ="%second_val,unery," binary of %d ="%first_val,bin," => ",unery+str(bin)[1:])
temp=unery+str(bin)[1:]
fst_value_bin=binary(number)
print("Binary of %d ="%number,fst_value_bin)
print("encripted value = ",temp+str(fst_value_bin)[1:])


# decoading
# bin=input("enter the binary : ")
# bin='00100101'
# ls=list(bin)
# count=0
# for x in ls:
#     if int(x)==0:count+=1
#     else:break
# decript=ls[count+1+count:]
# decript.insert(0,"1")
# print("".join(decript),end=" => ")
# decript=decript[::-1]
# dec=0
# for x in range(0,len(decript)):
#     dec+=(2**(x))*int(decript[x])
# print(dec)