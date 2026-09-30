'''
WAP to  swap two index values of the array. 
Swap index 1 and 5 elements:
Original array: [10,20,30,40,50,60,70]
Swapped array: [10,60,30,40,50,20,70]
'''
arr = [10,20,30,40,50,60,70]

arr[1], arr[5] = arr[5], arr[1]
print(arr)
