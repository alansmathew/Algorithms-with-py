def getContinue(ch):
    ch=input("Do you want to continue (y/n): ")
    if (ch=="Y" or ch=="y"):
        getContinue(ch)
    else:
        return
getContinue("Y")
