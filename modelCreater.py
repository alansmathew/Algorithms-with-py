resultFile = []

modelName = "ProfileModel"

def createStruct():
    print()
    # f = open("Result.txt", "a")
    # f.write("hello world")
    # f.close()

f = open("test.txt", "r")
data = f.readlines()
f.close()

# print(data)
for x in data: 
    x = x.strip()
    if x == '{\n' or x == '{':
        print("struct ",modelName,": decordable {")
    elif x == '}\n' or x == '}':
        print('}')
    else:
        fields = x.split(":")
        print(fields)
        if len(fields) > 1:
            print(fields[1])
            if fields[1].isdigit():
                print("number")
            # pass

print()

