"""
Write a program that stores a random number between 1 and 10.
The user has to guess the random number, the program should loop until they get it right.
Once the user has guessed the correct number, congratulate them and end the program.
"""

# import the random library
import random

# create a random number between 1 and 10 (inclusive)
random_number = random.randint(1,10)

# ask the user for a random number
user_guess = int(input("Guess a number between 1 and 10... \n")) # convert the guess from string to integer

while random_number != user_guess:
    print("Sorry, please try again")
    user_guess = int(input("Guess a number between 1 and 10... \n")) # convert the guess from string to integer

print(f"Well done, you guessed correctly - {user_guess}")




