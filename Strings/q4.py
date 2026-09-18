# Reverse sequence
# i/p -> Mohan is here
# o/p -> here is Mohan

def reverse(s):
    temp = ''
    res = ''

    for i in range(len(s)):
        c = s[i]
        if c!=' ':
            temp +=c

        if c==' ' or i==len(s)-1:
            res = temp+' '+res
            temp = ''
    return res.strip()

s = input("Enter a string: ")
print(reverse(s)) 
