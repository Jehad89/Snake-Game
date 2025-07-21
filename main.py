from turtle import Screen
from snake import Snake
import time
from food import Food
from score import Score


window = Screen()
window.setup(width=700, height=700)
window.title("Snake Game")
window.bgcolor('black')
window.tracer(0)


snake = Snake()
food = Food()
score = Score()


game_on = True
while game_on:
    snake.move()
    window.update()
    time.sleep(0.1)

    window.listen()
    window.onkey(snake.right,'Right')
    window.onkey(snake.up,'Up')
    window.onkey(snake.left,'Left')
    window.onkey(snake.down,'Down')

    if snake.head.distance(food) < 15:
        score.add_point()
        food.display_food()
        snake.extend()

    if snake.head.xcor() < -330 or snake.head.xcor() > 330 or snake.head.ycor() < -330 or snake.head.ycor() >330:
        game_on = False
        score.game_over()

    for turtle in snake.turtles[:-1]:
        if turtle.distance(snake.head) < 10:
            game_on = False
            score.game_over()


window.exitonclick()