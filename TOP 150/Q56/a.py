
#Implement binary search algorithm

# using loop

def binarySearch(a, target):
    low = 0
    high = len(a)-1
    count = 0
    while low <= high:
        count +=1
        mid = low + (high-low)//2
        if a[mid]==target:
            return mid, count
        elif a[mid]>target:
            high = mid - 1
        else:
            low = mid + 1
    return -1

a = [8,10,12,18,20,23,35,40,55]
res, count = binarySearch(a, 35)
print("Target at index: ",res)
print("Total iteration: ", count)



# Using Recursion

'''
def binarySearch(a, low, high, target):
    if low>high:
        return -1
    mid = low + (high-low)//2
    if a[mid]==target:
        return mid
    elif a[mid]>target:
        return binarySearch(a,low, mid-1, target)
    else:
        return binarySearch(a, mid+1, high, target)

a = [8,10,12,18,20,23,35,40,55]
print(binarySearch(a,0, len(a)-1, 35 ))
'''