'''
c) WAP to get average of all elements at even 
index of array.
'''


arr = [10,20,30,40,50,60,70,80,90,100]
sum = 0
count = 0
for i in range(len(arr)):
    if i%2==0:
        count +=1
        sum +=arr[i]

avg = sum/count
print(avg)