import sys

print("Choose your holiday package:")
print("L: luxury package\nS: standard package\nB: basic package ")

menu = input().strip()[:1].upper()   # read a line, trim, take first char, make uppercase
print(menu)
print(f"The {menu} package includes:")

if menu == 'L':
    print("\tSpa Day")
    print("\tSailboat Tour")
elif menu == "S":
    print("\tCity Tour")
    print("\tComplimentary Happy Hour")
elif menu == "S":
    print("\tAirport Transfers")
    print("\tComplimentary Breakfast")
else:
    print("Please select the L,S,B package.")
