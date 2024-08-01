#import re
#str = "GeeksforGeeks is best!"
#pattern = r'\w+'
#substrings = re.findall(pattern, str)
#print(substrings)



import re
s =input("Enter a string")
word=r'\w+'
substring=re.findall(word,s)
print("Total substrings:",len(substring))


print("-----------------------------")

s=input("Enter a string")
count=0
for i in s:
    if (i==" "):
        count=count+1
print("Total words are:",count+1)
