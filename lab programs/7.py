import string
print("String Functions")
str=input("Input a string : ")
# str='alan'
print('len(string)=',len(str)) # returns the length of string
print(str.lower()) #converts to lowercase
print(str.upper()) #converts to upper case
print(str.swapcase()) #swaps the case 
print(str.capitalize()) #will capalitize
print(str.title()) #converst to tilecase
print(str.lstrip('a')) #returns other char after the given char from left to right 
print(str.rstrip('n')) #returns other char after the given char from right to left 
print(str.strip('n'))  #compination of both lstrip and rstrip
print(max(str)) #max of string
print(min(str)) #min of string
print(str.center(10)) #returns center in 10 spaces before and after
print(str.ljust(10)) # if string is less than 10char puts white spaces after to make it 10 
print(str.rjust(10)) # if string is less than 10char puts white spaces before to make it 10
print(str.zfill(10)) #if string is less than 10char puts 0 before to make it 10
print(str.count("a", 0,len(str))) #returns how many times "a" repeates in 0 to length of str 
print(str.find("a",0,len(str))) #finds first mach to char "a" for 0 to length of str 
print(str.rfind("a", 0,len(str))) #finds last mach to char "a" for 0 to length of str
print(str.rindex("a",0,len(str))) #If substring exists inside the string, it returns the highest index in the string where substring is found..
 # difference is that rfind() returns -1 if the substring is not found, whereas rindex() throws an exception..
print(str.startswith("e",0,len(str))) # returns True if the string starts with the given prefix, otherwise it returns False 
print(str.endswith("n",0,len(str))) # returns True if a string ends with the given suffix otherwise returns False 
print(str.isdecimal()) #returns true if its decimal else false
print(str.isalpha()) #returns true if its alpahabat else false
print(str.isalnum()) #returns true if its alphanumeric else false
print(str.isdigit() )#returns true if its digit else false
print(str.islower()) #returns true if its lowercase else false
print(str.isupper()) #returns true if its supercase else false
print(str.isnumeric()) #returns true if its numeric else false
print(str.isspace()) #returns true if its have some space else false
print(str.istitle()) #returns true if its title case else false
print(str.expandtabs(3)) # control for tab spaces, if str="abc \tdef" prints abc   def 
print("".join(str)) #returns a string concatenated with the elements if ls=[1,2,3] prints 123; before join should be whitespace or nedded charactor; here "" 
print(str.split()) #charactors will split at specified seperators
print(str.splitlines()) #is used to split the lines at line boundaries