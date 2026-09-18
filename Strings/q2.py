'''
Palindrome string
'''

def palindrome_string(s):
    res = ''
    for i in s:
        res = i + res
    if res == s:
        print(f"{s} == {res} is palindrome string")
    else:
        print(f"{s} != {res} is not a palindrome string")


s = input("Enter a string: ")
palindrome_string(s)