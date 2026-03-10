"""
Number Guessing Game 🎮
Author: Your Name
Description:
A simple number guessing game where the computer generates
a random number between 1 and 100 and the user tries to guess it.
"""

import random

# Generate random number between 1 and 100
jackpot_number = random.randint(1, 100)

# Track number of attempts
attempts = 0

print("🎮 Welcome to the Number Guessing Game!")
print("I have selected a number between 1 and 100.")
print("Try to guess it!\n")

while True:
    try:
        user_guess = int(input("Enter your guess: "))
        attempts += 1

        if user_guess < jackpot_number:
            print("Too low! Try a greater number.\n")

        elif user_guess > jackpot_number:
            print("Too high! Try a smaller number.\n")

        else:
            print("\n🎉 Correct! You guessed the number.")
            break

    except ValueError:
        print("⚠ Please enter a valid number.\n")

# Final results
print(f"\n✅ The correct number was: {jackpot_number}")
print(f"🏆 Your score (number of attempts): {attempts}")

# Score feedback
if attempts <= 5:
    print(" Excellent! You're a guessing master.")
elif attempts <= 10:
    print(" Good job!")
else:
    print(" You got it, but try to guess faster next time!")

