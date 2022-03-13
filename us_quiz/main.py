import turtle as t
import pandas as pd

image = "./us_quiz/blank_states_img.gif"
csv = "./us_quiz/50_states.csv"

screen = t.Screen()
map = t.Turtle()
state = t.Turtle()
screen.title("US Quiz")
screen.addshape(image)
map.shape(image)

data = pd.read_csv(csv)
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < len(data):
  answer = screen.textinput(title=f"{len(guessed_states)}/{len(all_states)} Correct", prompt="Type in state name.").title()

  if answer in all_states and answer not in guessed_states:
    state_data = data[data.state == answer]
    state.penup()
    state.goto(int(state_data.x), int(state_data.y))
    state.write(state_data.state.item())
    guessed_states.append(state_data.state.item())
  elif answer == "Exit":
    missing_states = [state for state in all_states if state not in guessed_states]
    new_data = pd.DataFrame(missing_states)
    new_data.to_csv("states_to_learn.csv")
    break
