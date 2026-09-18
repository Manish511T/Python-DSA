def selection_sort(a):
    for i in range(len(a)-1):
        min = a[i]
        min_index = i
        for j in range(i+1, len(a)):
            if a[j]<min:
                min = a[j]
                min_index = j
        a[min_index] = a[i]
        a[i] = min
    return a

arr = eval(input("Enter a list : "))
print(selection_sort(arr))
