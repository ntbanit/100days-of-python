from art import logo
print(logo)

print("""
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
""")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
lives = 10
if difficulty == 'hard':
    lives = 5

import random
CHOOSEN_NUMBER = random.randint(1, 100)

while lives > 0 :
    print(f"You have {lives} attempts remaining to guess the number.")
    number = int(input("Make a guess: "))
    if number == CHOOSEN_NUMBER :
        print("Exactly! You win!")
        break

    lives -= 1
    if number > CHOOSEN_NUMBER :
        print("Too high!")
    else :
        print("Too low!")

if lives == 0:
    print(f"You lose! Exacly one is {CHOOSEN_NUMBER}")