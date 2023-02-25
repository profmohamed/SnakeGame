import time
from turtle import Screen
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

sanke = Snake()

screen.listen()
screen.onkey(sanke.up, "Up")
screen.onkey(sanke.down, "Down")
screen.onkey(sanke.left, "Left")
screen.onkey(sanke.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    sanke.move()


screen.exitonclick()
