target = 55
guess = -1

while guess != target:
    guess = int(input("Guess a number between 0 and 100 (-1 to quit): "))
    if guess < target:
        print("This number is lower than the target number.")
    elif guess > target:
        print("This number is higher than the target number.")
    else:
        print("You guessed the target!")
        
    if guess == -1:
        print("Good bye!")
        break
    