def moderateDays():
    lst=[]
    dic={"monday":68,"tuesday":70,"wednessday":73,"thursday":69,"friday":65,"saturday":71,"sunday":72}
    for key in dic.keys():
        if dic.get(key)>=70 and dic.get(key)<=79 :
            lst.append(key)
    return lst
print(moderateDays())
