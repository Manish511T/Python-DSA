'''
a) Problem Statement:
You are given an amount of money N (in rupees) and
different coin denominations. Determine how many
coins of each denomination are required to represent
the given amount using the minimum number of coins.
i/p:
amount = 98 denominations = [50, 25, 20, 10, 5, 1]
o/p: 50 -> 1 25 -> 1 20 -> 1 10 -> 0

5 -> 0 1 -> 3
'''

amount = 98
denominations = [50,25,20,10,5,1]

for i in denominations:
    count = amount//i
    print(i, "->", count)
    amount = amount%i
