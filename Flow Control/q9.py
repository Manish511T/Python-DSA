# WAP to take total shopping price and provide
# discounted price as per below condition
# 40% discount if price>=10000
# 30% discount if price>=6000
# 20% discount if price>=3000
# 8% discount if price>=1

price = float(input("Enter total shopping price: "))

if price >= 10000:
    discount = 40
elif price >= 6000:
    discount = 30
elif price >= 3000:
    discount = 20
else:
    discount = 8

discount_amount = price * discount / 100
final_amount = price - discount_amount

print("Discount:", discount, "%")
print("Discount Amount:", discount_amount)
print("Final Price:", final_amount)