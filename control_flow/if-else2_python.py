skin = (input("Would you like an animal with fur(f), feathers(t), or scales(s)?") )
print(skin)

if skin == 'f':
    print("Get a dog")
elif skin == 't':
    print("Get a bird")
elif skin == 's':
    location = (input("Would you like an animal that lives in water(w), land(l), or both(b)?"))
    print(location)

    if location == 'w':
        print('Get a fish')
    elif location == 'l':
        print('Get a gecko')
    elif location == 'b':
        print('Get a frog')
    else:
        print('Please enter water(w), land(l), or both(b)')
else:
    print('Please choose fur(f), feathers(t), or scales(s)')
