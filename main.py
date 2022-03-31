from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
with open("high_score.txt") as file:
    contents = file.read()
    print(contents)
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
scoreboard = 0
snake = Snake()
food = Food()
scoreboard = Scoreboard()
#MOVE SNAKE HEAD BY UP DOWN LEFT RIGHT ARROW KEYBOARD KEYS
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
#screen.update()
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    #for seg_num in range(start=2, stop=0, step =-1):
    snake.move()
    #detect collision between snake and food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #Detect collision with wall
    if snake.head.xcor() == 280 or snake.head.xcor() == -280 or snake.head.ycor() == 300 or snake.head.ycor() == -300:
        scoreboard.reset()
        snake.reset()

    #Detect collision with own tail
    #for segment in snake.segments[1:len(snake.segments)-1]:
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()




screen.exitonclick()