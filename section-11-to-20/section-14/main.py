import art
from game_data import data
import os
import random

current_score = 0

def display(compare_as, person):
    pronoun = "a"
    first_char = person['description'][0].lower()
    if first_char in "aiueo":
        pronoun = "an"
    print(f"{compare_as}: {person['name']}, {pronoun} {person['description']}, from {person['country']}.")

def print_logo():
    os.system("cls")
    print(art.logo)

def play_one_round(A, B):
    display("Compare A", A)
    print(art.vs)
    display("Against B", B)
    choice = input("Who has more followers? Type 'A' or 'B': ").upper()

    global current_score
    if choice == 'A' and A['follower_count'] > B['follower_count'] or choice == 'B' and B['follower_count'] > A['follower_count']:
        current_score += 1
        print_logo()
        print(f"You're right! Current score: {current_score}.")
        return choice

    print_logo()
    print(f"Sorry, that's wrong. Final score: {current_score}")

# last winner will be A
print_logo()
last_winner = random.choice(data)
while True :
    A = last_winner
    B = random.choice(data)
    while A == B :
        B = random.choice(data)

    result = play_one_round(A, B)
    if result == None :
        break
    # set the last winner, also remove the loser to the game
    if result == 'A':
        last_winner = A
        data.remove(B)
    else:
        last_winner = B
        data.remove(A)