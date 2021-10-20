cr=int(input("Enter the credit : "))
print("Senior Status" if cr >= 90  else "Junior Status" if cr >=60 and cr < 90 else "Sophomore Status" if cr>=30 and cr<60 else "Freshman Status")
