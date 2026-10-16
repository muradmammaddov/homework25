purchase = int(input("Enter purchase amount: "))
if purchase < 100:
    discount = 0
elif 100 <= purchase < 300:
    discount = 10
elif 300 <= purchase < 500:
    discount = 15
elif 500 <= purchase:
    discount = 20

print("Original price: ", purchase)
print("Discount: ", discount)
print("Final price: ", purchase - purchase * discount/100)