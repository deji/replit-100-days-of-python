# from getpass import getpass
import random

print("Guess the Number game!")
print()
number2Guess = random.randint(1, 10)
print("Can you guess the number I picked between 1 and 10? 👹👹")
print()

attempts = 0

while True:
    guessedNumber = int(
        input(
            "Player 2, guess the number; between 1 and 10 and enter a negative number to quit: "
        ))
    if guessedNumber < 0:
        print("You quit!")
        exit()
    elif guessedNumber > 1000000:
        print("Sorry! That's too big. It should be between 1 and 10.")
        continue
    elif guessedNumber < number2Guess:
        print("Too low!")
        attempts += 1
        continue
    elif guessedNumber > number2Guess:
        print("Too high!")
        attempts += 1
        continue
    else:
        print("You guessed it!")
        attempts += 1
        break

print("It took you", attempts, "attempts to guess the number!")
print("Thanks for playing!")
