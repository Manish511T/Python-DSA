'''
Reverse sequence of word in string
s='Hello Python'
o/p -> 'Python Hello'
'''
def reverse_sequence(s):
    temp = ''
    result = ''

    for i in range(0,len(s)):
        c = s[i]

        if c!=' ':
            temp = temp+c
        
        if c == ' ' or i == len(s)-1:
            result = temp+' '+result
            temp = ''
    return result.strip()



s = input("Enter a string to reverse: ")
print(reverse_sequence(s))
