weight = float(input("Weight: "))
unit = input("(L)bs or (K)g: ")

if unit.upper() == "L":
    converted = (weight * 0.45)
    print(f"You are {converted} kilograms")
elif unit.upper() == "K":
    converted = weight / 0.45
    print(f"You are {converted} pounds")

