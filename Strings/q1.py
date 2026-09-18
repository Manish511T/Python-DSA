'''
Reverse The String
i/p -> s = "Mohan is here"
o/p -> "ereh si nahoM"
'''

#Method 1
'''

def reverse(s):
    temp = ''
    res = ''

    for i in s:
        if i != ' ':
            temp = i+temp
        else:
            res = temp+' '+res
            temp = ''

    return temp+' '+res

s = input("Enter a string: ")
print(reverse(s)) 

'''
# Method 2
def reverse(s):
    temp = ''
    res = ''
    for i in range(len(s)):
        c = s[i]
        if c!=' ':
            temp = c+temp
        if c==' ' or i==len(s)-1:
            res = temp+' '+res
            temp=''
    return res.strip()


s = input("Enter a string: ")
print(reverse(s)) 