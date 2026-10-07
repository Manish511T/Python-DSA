# Sum Unique elements

def sumUniqueElements(a):
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

    sum = 0
    for i in range(len(freq)):
        if freq[i]==1:
            sum += i+min

    print(sum)

a = eval(input("Enter value in an array: "))
sumUniqueElements(a)