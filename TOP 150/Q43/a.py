# WAP to print the element and its frequency which has appeared for the maximum time in the array.

def maxfrequency(a):
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

    maxFreq = freq[0]
    maxElement = min
    for i in range(len(freq)):
        if freq[i]>maxFreq:
            maxFreq = freq[i]
            maxElement = i+min

    print(maxElement)
    print(maxFreq)


a = eval(input("Enter value in an array: "))
maxfrequency(a)