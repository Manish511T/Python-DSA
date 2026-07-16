# For a given three-digit number int n=578;
# Print each digit of the number one by one from
# Right to Left.
# o/p:
# 8
# 7
# 5

n = 578

while n>0:
    print(n%10)
    n //=10