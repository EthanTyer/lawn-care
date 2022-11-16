Name = input("Enter your name\n> ")
Address = input("Enter your address\n> ")
Phonenum = input("Enter your phone number\n> ")

width = int(input("Enter the lawn width in metres\n> "))
length = int(input("Enter the lawn length in metres\n> "))
sqrMeters = width * length

LawnCareCost = 1
while True:
    quality = input("Enter the quality of lawn service you wish for:\nNone // Economy // Standard // Luxury\n> ")
    if quality == "None":
        break
    elif quality == "Economy":
        LawnCareCost = 0.45
        break
    elif quality == "Standard":
        LawnCareCost = 0.8
        break
    elif quality == "Luxury":
        LawnCareCost = 1.15
        break
    else:
        print("Please enter a valid lawn quality service, as indicated above.")

CostSqrMeters = sqrMeters * 0.5
LawnCareFactored = CostSqrMeters * LawnCareCost
TotalCost = LawnCareFactored * 1.2

print(f"Name: {Name}\nAddress: {Address}\nPhone Number: {Phonenum}\n"
      f"Total Cost: £{TotalCost}")
