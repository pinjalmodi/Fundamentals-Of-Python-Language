#Write a Python program to get the Factorial number of given number.


fact=1
n = int(input("Enter a number to find it's factorial"))
for i in range(1,n+1):
    fact=fact*i
print("Factorial is",fact)
