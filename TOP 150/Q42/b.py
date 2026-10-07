# Remove duplicates

def removeDuplicates(a):
    max=a[0]
    min=a[0]

    for i in a:
        if i>max:
            max = i
        elif i<min:
            min = i

    freq = [0]*(max-min+1)

    for i in a:
        freq[i-min] +=1

    for i in range(len(freq)):
        if freq[i]>0:
            print(i+min, end=' ')

a = eval(input("Enter value in an array: "))
removeDuplicates(a)