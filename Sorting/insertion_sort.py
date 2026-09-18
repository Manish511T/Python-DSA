def insertion_sort(a):
    for i in range(1, len(a)):
        pivot = a[i]
        j = i-1
        while j>=0 and a[j]>pivot:
            a[j+1] = a[j]
            j -=1
        a[j+1] = pivot

    return a

arr = eval(input("Enter a list : "))
print(insertion_sort(arr))
