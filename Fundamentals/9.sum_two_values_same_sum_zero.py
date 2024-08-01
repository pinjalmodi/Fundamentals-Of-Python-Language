#Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.

a = int(input("Enter 1st value"))
b = int(input("Enter 2nd value"))
c = int(input("Enter 3rd value"))

if (a==b or b==c or c==a):
  print("Sum is",0)
else:
  print("Sum is",a+b+c)

