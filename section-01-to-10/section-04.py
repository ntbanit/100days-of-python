rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


def display_choice(player_choice):
    if player_choice == "R":
        print(rock)
    elif player_choice == "P":
        print(paper)
    elif player_choice == "S":
        print(scissors)
    else :
        print("Wrong Input")
        exit(0)

def result_game(player_choice, computer_choice):
    if player_choice == computer_choice :
        return "Draw"
    if player_choice == "R" and computer_choice == "S"\
            or player_choice == "P" and computer_choice == "R"\
            or player_choice == "S" and computer_choice == "P":
        return "You Win! Computer Lose"
    return "You Lose! Computer Win."