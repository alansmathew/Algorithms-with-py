def read():
    fl=open("Myprofile.txt","r")
    lst=(fl.readlines())
    for x in lst:
        print(x)
    fl.close()
read()
fl=open("Myprofile.txt","a")
course="\ncourse : "+input("Enter course name: ")
teacher="\nclass teacher : "+ input("Enter class teachers name: ")
fl.writelines(course)
fl.writelines(teacher)
fl.close()
read()