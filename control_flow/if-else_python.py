# python

TARGET =33
guess = int(input("Guess a number between 0-100\n"))
print(f'You guess: {guess}')

if guess < TARGET:
    print('Your guess is too low.')
elif guess > TARGET:
    print('Your guess is too high.')
else:
    print('Yay! Your guessed correctly.\n')


