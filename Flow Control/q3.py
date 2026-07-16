# WAP to take a character input and print it
# is alphabet or not using if else statement.

ch = input("Enter a character: ")[0]

if 'a'<=ch<='z' or 'A'<=ch<='Z':
    print(ch, " is alphabet")
else:
    print(ch, " is not a alphabet")

