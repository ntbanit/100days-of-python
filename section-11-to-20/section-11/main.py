import os
import random
from art import logo

CARDS = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
TARGET_SCORE = 21
MIN_SCORE = 16
ACE = 11
SMALL_ACE = 1

def draw_first_cards():
    global CARDS
    output_cards = []
    output_cards.append(random.choice(CARDS))
    output_cards.append(random.choice(CARDS))
    return output_cards

def check_blackjack(computer_cards, your_cards):
    """Detect when computer or user has a blackjack. (Ace + 10 value card).
    If computer gets blackjack, then the user loses (even if the user also has a blackjack).
    If the user gets a blackjack, then they win (unless the computer also has a blackjack)."""
    global TARGET_SCORE
    your_score = sum(your_cards)
    computer_score = sum(computer_cards)
    if computer_score == TARGET_SCORE :
        print("You lost. Computer gets blackjack!")
        return True
    if your_score == TARGET_SCORE:
        print("You win. You got blackjack!")
        return True
    return False

def cal_score(hand_cards):
    score = sum(hand_cards)
    global TARGET_SCORE
    global ACE
    global SMALL_ACE
    if score > TARGET_SCORE and ACE in hand_cards :
        hand_cards = [SMALL_ACE if x == ACE else x for x in hand_cards]
        score = sum(hand_cards)
    return score

def computer_draw(computer_cards, your_score):
    global TARGET_SCORE
    if your_score > TARGET_SCORE:
        return computer_cards

    computer_score = cal_score(computer_cards)
    global MIN_SCORE
    global CARDS
    while computer_score < TARGET_SCORE and computer_score <= MIN_SCORE :
        computer_cards.append(random.choice(CARDS))
        computer_score = cal_score(computer_cards)
    return computer_cards

def draw_result(computer_cards, your_cards):
    computer_score = cal_score(computer_cards)
    your_score = cal_score(your_cards)
    print(f"\tYour final hand:{your_cards}, final score: {your_score}")
    print(f"\tComputer's final hand:{computer_cards}, final score: {computer_score}")

    if your_score > TARGET_SCORE:
        print("You lost.")
    elif computer_score > TARGET_SCORE:
        print("You win")
    elif computer_score == your_score:
        print("Result: Draw.")
    elif computer_score > your_score:
        print("You lost.")
    else:
        print("You win.")

while True :
    play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if play_game == 'n':
        break

    os.system("cls")
    print(logo)

    computer_cards = draw_first_cards()
    your_cards = draw_first_cards()

    if check_blackjack(computer_cards, your_cards):
        print(f"\tYour final hand: {your_cards}")
        print(f"\tComputer's final hand: {computer_cards}")
        continue

    your_score = cal_score(your_cards)
    while your_score < TARGET_SCORE:
        print(f"\tYour cards: {your_cards}, current score: {your_score}")
        print(f"\tComputer's first card: {computer_cards[0]}")

        confirm = input("Type 'y' to get another card, type 'n' to pass: ")
        if confirm == 'n':
            break
        your_cards.append(random.choice(CARDS))
        your_score = cal_score(your_cards)

    computer_cards = computer_draw(computer_cards, your_score)
    draw_result(computer_cards, your_cards)