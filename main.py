from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
screen.bgcolor("black")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
FONT = ("Courier", 18, "bold")
result = Turtle()
result.hideturtle()
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)
user_bet = screen.textinput(title="Make your bet", prompt=f"Which turtle will win the race: Red, Orange, Yellow, Green, Blue or Purple? \n{'Enter a color:'.center(120)} ")
if user_bet in colors:
    is_race_on = True
else:
    while user_bet not in colors:
        user_bet = screen.textinput(title="Error",prompt="Choose from: Red, Orange, Yellow, Green, Blue or Purple :")
        if user_bet in colors:
            is_race_on = True



while is_race_on:

    for turtle in all_turtles:
        #230 is 250 - half the width of the turtle.
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            result.pencolor(winning_color)
            if winning_color == user_bet:
                result.write(f"You Win", align="center", font=FONT)
            else:
                result.write(f"You Lose.\n{winning_color.capitalize()} turtle Wins", align="center", font=FONT)


        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
