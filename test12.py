distance = float(input("Enter the distance: "))
starting_fee = 2.00
if distance < 0:
    print("Negative distance")
else:
    if distance > 0 and distance <=5:
        rate = 0.7
    elif distance > 5 and distance <=15:
        rate = 0.6
    elif distance > 15:
        rate = 0.5
    distance_fee = distance * rate
    total_fare = distance_fee + starting_fee

    print("Starting fee:", starting_fee, "AZN")
    print("Distance fee:", distance_fee, "AZN")
    print("Total fare:", total_fare, "AZN")