import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 51:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States guessed", prompt="What's the another state's name?").title()
    print(answer_state)

    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in  guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("Missing_states")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        states_coor = data[data.state == answer_state]
        t.goto(states_coor.x.item(), states_coor.y.item())
        t.write(answer_state)