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

number=int(input("Enter encoding number: "))

unery=encoading(int(math.log(number,2))+1)
bin=binary(number)

print("1+log2(%d)="%number,int(math.log(number,2))+1, "unery = %s"%unery)
print("binary of %d ="%number,bin)
print("Encorded = ", unery+str(bin)[1:])

# decoarding


