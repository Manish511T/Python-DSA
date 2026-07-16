# WAP to check the given year is a Leap
# year or NOT.

year = int(input("Enter a year: "))

if (year%4==0 and year%100 !=0) or year%400==0:
    print("Leap year")
else:
    print("not a Leap year")
