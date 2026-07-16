# Method 1
'''
def check_palindrome(s,length):
    start = 0
    end = length-1

    while start<end:
        if s[start]!=s[end]:
            return False
        start +=1
        end -=1
    return True
'''

# Method 2
def check_palindrome(s,length):
    rev = s[::-1]
    if s==rev:
        return True
    else:
        return False
    


s = input("Enter a string to reverse: ")
isPalindrome=check_palindrome(s,len(s))
if isPalindrome:
    print(s," is a palindrome string")
else:
    print(s," is not a palindrome string")


