# Sample program for "Pointer-like" behavior in Python

# Step 1: Declare variables
givenInt = int(input("integer = "))
givenFloat = float(input("float = "))
givenDouble = float(input("double = "))   # Python's float is double-precision
givenChar = input("character = ")[0]      # take only the first character
givenString = input("string = ")

# Step 2: Print the values
print("\n--- Values stored in variables ---")
print("integer =", givenInt)
print("float =", givenFloat)
print("double =", givenDouble)
print("string =", givenString)
print("character =", givenChar)

# Step 3: Print their 'addresses' using id()
print("\n--- Memory addresses (id) ---")
print("address of integer =", hex(id(givenInt)))
print("address of float   =", hex(id(givenFloat)))
print("address of double  =", hex(id(givenDouble)))
print("address of string  =", hex(id(givenString)))
print("address of char    =", hex(id(givenChar)))

# Step 4: Simulate pointer-like behavior
pointerGivenInt = givenInt
pointerPointerGivenInt = pointerGivenInt

print("\n--- Pointer-like simulation ---")
print("pointerGivenInt (value copy) =", pointerGivenInt)
print("pointerPointerGivenInt (value copy) =", pointerPointerGivenInt)

# Step 5: Show that they reference the same object
print("\n--- Check if they refer to the same object ---")
print("id(givenInt) == id(pointerGivenInt):", id(givenInt) == id(pointerGivenInt))
print("id(pointerGivenInt) == id(pointerPointerGivenInt):", id(pointerGivenInt) == id(pointerPointerGivenInt))
