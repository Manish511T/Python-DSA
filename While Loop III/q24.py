s = input("Enter a string: ")
start = 0
end = len(s)-1
flag = True
while start<end:
    if s[start] !=s[end]:
        flag = False
        break
    start +=1
    end -=1

if flag:
    print(s, " is a palindrome ")
else:
    print(s, " is not a palindrome ")