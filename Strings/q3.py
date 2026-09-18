def reverse(s):
    temp = ''
    res = ''

    for i in range(len(s)):
        c = s[i]

        if c!=' ':
            temp = c+temp

        if c == ' ' or i==len(s)-1:
            res +=' '+temp
            temp = ''
    return res.strip()

s = input("Enter a string: ")
print(reverse(s)) 
