number = None
character = None
sentence = None

# "Pointer" variables (just more references)
pointerI = number
pointerC = character
pointerS = sentence

# Assign values through direct reference
number = 45
character = 'f'
sentence = "Hey look at me, I know pointers!"

# Show results
print("number =", number)
print("character =", character)
print("sentence =", sentence)

# Show that variables are references to objects (like memory addresses)
print("\n--- Memory info (id values) ---")
print("id(number):", id(number))
print("id(pointerI):", id(pointerI))
print("id(character):", id(character))
print("id(pointerC):", id(pointerC))
print("id(sentence):", id(sentence))
print("id(pointerS):", id(pointerS))