import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.setup(width=725, height=491)
screen.addshape(image)

turtle.shape(image)

import pandas as pd 
data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()

guessed_states = []
while len(guessed_states) < len(all_states):
    guess_state = screen.textinput(title=f"{len(guessed_states)}/{len(all_states)} Guessed", prompt="What's state name?")
    print(guess_state)
    if guess_state is None or guess_state == "exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    elif guess_state in guessed_states:
        print("You already guessed this state.")
    elif guess_state in all_states:
        guessed_states.append(guess_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == guess_state]
        t.goto(int(state_data.x.item()), int(state_data.y.item()))
        t.write(guess_state, align="center", font=("Arial", 5, "normal"))
        print("Correct")

turtle.mainloop()