
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

score = Scoreboard()
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)
screen.listen()

paddle_r = Paddle((350,0))
paddle_l = Paddle((-350,0))
ball =  Ball()

screen.onkey(paddle_r.go_up, "Up")
screen.onkey(paddle_r.go_down, "Down")
screen.onkey(paddle_l.go_up, "w")
screen.onkey(paddle_l.go_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # collision with top down
    if ball.ycor() > 280 or ball.ycor()<-280:
        ball.bounce_y()
        
    
#  collision with paddle
    if ball.distance(paddle_r) < 50 and ball.xcor() > 320 or ball.distance(paddle_l) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        
       
#right paddle collision
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()
    
#left paddle collision
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()


screen.exitonclick()