# WAP to take CP and SP and print %Profit
# or % Loss in the transaction.

CP = int(input("Enter cost prize: "))
SP = int(input("Enter selling prize: "))

if SP > CP:
    profit = ((SP-CP)/CP)*100
    print(profit, "% Profit")
elif SP < CP:
    loss = ((CP-SP)/CP)*100
    print(loss, "% Loss")
else:
    print("No Profit, No Loss")