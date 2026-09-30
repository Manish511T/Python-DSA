'''
For the given array of Strings, print the 
largest string
'''

arr = ['Hello', 'Nice', 'Blunt', 'original']
largest_string = ''
for i in arr:
    if len(i)>len(largest_string):
        largest_string = i

print(largest_string)