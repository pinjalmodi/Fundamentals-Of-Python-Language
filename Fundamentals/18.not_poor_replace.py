#Write a Python program to find the first appearance of the substring
#'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the
#whole 'not'...'poor' substring with 'good'. Return the resulting string

s=input("Enter a string")

x=s.find('not')
y=s.find('poor')

if (y>x) and (y>0) and (x>0):
    s=s.replace(s[x:(y+4)],'good')
    print("New Substring is",s)
