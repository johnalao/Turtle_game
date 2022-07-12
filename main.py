from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
bet = screen.textinput(title="Make a bet", prompt="Which turtle would likely win this race, Enter a color: ").lower()
color = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
y_positions = [-100, -70, -40, -10, 20, 50]
all_turtles = []


for turtle_name in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color[turtle_name])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_name])
    all_turtles.append(new_turtle)
if bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == bet:
                print(f"You've won, the {winning_turtle} turtle won the race")
            else:
                print(f"You've lost, the {winning_turtle} turtle won the race")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
