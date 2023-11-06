from turtle import Turtle, Screen
from padle import Padle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_padle = Padle((350, 0))
l_padle = Padle((-350, 0))


ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=r_padle.up, key="Up")
screen.onkey(fun=r_padle.down, key="Down")
screen.onkey(fun=l_padle.up, key="w")
screen.onkey(fun=l_padle.down, key="s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)  # Sets default ball speed.
    screen.update()
    ball.move()

    # Detect collision with upper and lower wall:
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with r_paddle and l_paddle:
    if (
        ball.distance(r_padle) < 50
        and ball.xcor() > 320
        or ball.distance(l_padle) < 50
        and ball.xcor() < -320
    ):
        ball.bounce_x()

    # Detect r_paddle miss:
    if ball.xcor() > 380:
        ball.reset_right()
        scoreboard.l_point()

    # Detect l_paddle miss:
    if ball.xcor() < -380:
        ball.reset_left()
        scoreboard.r_point()


screen.exitonclick()
