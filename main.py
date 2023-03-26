from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("the Sanke game")

screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")  # setting up the up arrow key to move the snake up
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()


    eat= []
    if snake.head.distance(food) < 15:
        eat.append("eat eat eat")
        
        food.refresh()  # creating a new instance of the food
        snake.extend()
        scoreboard.increase_score()  # increasing the score
    print(eat)
    # checking if the snake has collided with the wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        print("GAmE OVER")
        scoreboard.game_over()
        game_is_on = False  # ending the game loop

    # checking if the snake has collided with its own tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.game_over()  # displaying the game over message
            game_is_on = False

screen.exitonclick()  # closing the screen when the user clicks on it
