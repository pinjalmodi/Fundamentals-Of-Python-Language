#Write a Python function that takes a list of words and returns the length
#of the longest one.


def longest(a):
    max=" "
    max_len=0
    for i in a:
        if len(i)>max_len:
            max=str(i)
            max_len=len(i)
    return max_len,max

length,longest_str=(longest(['a','ab','abc','abcd']))
print(length)
print(longest_str)
