# WAP to print frequency of each element of the array

def printFrequency(a):
    max = a[0]
    min = a[0]

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
            print(f"{i+min} is: {freq[i]} times")

a = eval(input("Enter value in an array: "))
printFrequency(a)