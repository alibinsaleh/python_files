# Guess a number
import random

secret_number = random.randint(1,100)
tries = 0
while True:
    guess = int(input('Please guess a number between 1 and 100: '))
    tries += 1
    if guess > secret_number:
        print('You are way over, guess again.')
    elif guess < secret_number:
        print('You are way below, guess again.')
    else:
        print(f'Correct, you guessed it in {tries} tries.')
        break

