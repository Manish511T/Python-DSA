def mostFrequency(a):
    max = a[0]
    min = a[0]

    for i in a:
        if i>max:
            max =i
        elif i<min:
            min =i

    freq = [0]*(max-min+1)

    for i in a:
        freq[i-min] +=1

    mostFreq = freq[0]
    mostFreqElement = None

    for i in range(len(freq)):
        if freq[i]>mostFreq:
            mostFreq = freq[i]
            mostFreqElement = i+min
    print(mostFreqElement)

a = eval(input("Enter value in an array: "))
mostFrequency(a)