a = 0

# First while loop
while a < 5:
    print(f"a = {a}")
    a += 1
    if a == 3:
        break
print("The first statement after the first while looping.")

# Second while loop
while a < 15:
    print(f"a = {a}")
    a += 1
    if a == 10:
        print("\tWhen a=10, go back to the top of the loop")
        print("\tThis means a=10 is skipped.\n")
        continue

print(f"After continue a = {a}")
