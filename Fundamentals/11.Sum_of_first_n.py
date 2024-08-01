#Write a python program to sum of the first n positive integers.

n = int(input("Enter the limit"))
sum=0
for num in range(1,n+1):
    sum=sum+num
print("Sum:",sum)
