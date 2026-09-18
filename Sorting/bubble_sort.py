def bubble_sort(a):
    for i in range(len(a)-1):
        flag = True
        for j in range(len(a)-1-i):
            if a[j]>a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                flag = False
        if flag:
            return a

    return a

arr = eval(input("Enter a list : "))
print(bubble_sort(arr))

            