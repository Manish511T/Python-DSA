'''
Reverse each word but keep only one space in string
s='Hello            Python'
o/p -> 'olleH nohtyP' 
'''
def reverse_each_word(s):
    temp=''
    result=''

    for i in range(0, len(s)):
        c = s[i]
        
        if c != ' ':
            temp = c+temp
        
        if (c == ' ' or i==len(s)-1) and len(temp)>0:
            result = result+' '+temp
            temp = ''
    return result.strip()

s = input("Enter a string to reverse: ")
print(reverse_each_word(s))