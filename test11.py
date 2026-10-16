usage = float(input("Enter monthly usage: "))
if usage > 0 and usage <= 100:
    rate = 0.08
elif usage > 100 and usage <= 300:
    rate = 0.12
elif usage > 300:
    rate = 0.15
print("Display usage:", usage)
print("Applied rate:", rate)
print("Total bill", usage * rate)