from turtle import Turtle, Screen
import random

is_race_on = False

screen = Screen()

screen.setup(height=400, width=500)
user_bet = screen.textinput(title="Make your bet", prompt="which turtle will win the race?select the colour: ")
colors = ["red", "yellow", "green", "blue", "purple", "orange"]
y_pos = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for num in range(0, 6):
    tim = Turtle(shape="turtle")
    tim.color(colors[num])
    tim.penup()
    tim.goto(x=-230, y=y_pos[num])
    all_turtles.append(tim)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print(f"You've won! The {winning_turtle} is the winner.")
            else:
                print(f"You've lost! The {winning_turtle} is the winner.")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()