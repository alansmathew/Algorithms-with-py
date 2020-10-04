def encoading(num):
    s=""
    for x in range(num-1):
        s+=str(0)
    return s+str(1)

def decoading(num):
    return len(str(num))

num=int(input("Enter a number:"))
print("encoarded= ",encoading(num))
print("decoaded= ",decoading(encoading(num)))