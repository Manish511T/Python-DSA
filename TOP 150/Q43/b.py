def leastFrequency(a):
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

    minFreq = freq[0]
    minElement = None
    for i in range(len(freq)):
        if freq[i]<minFreq and freq[i]>0:
            minFreq = freq[i]
            minElement = i+min
    print(minElement)

a = eval(input("Enter value in an array: "))
leastFrequency(a)