'''
WAJP to generate table of a number by using
recursion.
'''

def table(n, count=1):
    if count>10:
        return

    print(f"{n}x{count}={n*count}")
    table(n, count+1)

table(2)