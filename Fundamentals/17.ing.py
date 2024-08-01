#Write a Python program to add 'ing' at the end of a given string (length
#should be at least 3). If the given string already ends with 'ing' then add
#'ly' instead if the string length of the given string is less than 3, leave it
#unchanged.
x=input("Enter a string")
if len(x)>=3 and (x.endswith("ing")==False):
    print(x+"ing")
elif(x.endswith("ing")==True):
    print(x+"ly")
else:
    print(x)
    
