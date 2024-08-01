#Write a Python program to count the number of characters (character
#frequency) in a string


s=input("Enter a string")
char={}

for i in s:
    if i in char:
        char[i]=char[i]+1
    else:
        char[i]=1
print("Total characters",char)
