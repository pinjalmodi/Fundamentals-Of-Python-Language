#Write a Python program to get a single string from two given strings,
#separated by a space and swap the first two characters of each string.

#import random
#l=["String1","No2Strin"]
#print(random.choice(l))

a=input("Enter String1")
b=input("Enter String2")

x=b[0:2]+a[2:]
y=a[0:2]+b[2:]

print(x+" "+y)

