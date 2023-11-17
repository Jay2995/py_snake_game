from turtle import Screen, Turtle;
import random;
import time;
from snake import Snake;
from food import Food;
from scoreboard import Scoreboard;


screen = Screen();

screen.setup(width=600, height=600);
screen.bgcolor("black");
screen.title("The python snake game");
screen.tracer(0);


snake = Snake();
food = Food();
scoreboard = Scoreboard();


screen.listen();
screen.onkey(snake.up, "Up");
screen.onkey(snake.down, "Down");
screen.onkey(snake.left, "Left");
screen.onkey(snake.right, "Right");


game_is_on = True;

while game_is_on:
    screen.update();
    time.sleep(0.1);
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh();
        scoreboard.score += 1;
        scoreboard.update_score();
        snake.extend();

    if (snake.head.xcor() > 300) or (snake.head.xcor() < -300) or (snake.head.ycor() > 300) or (snake.head.ycor() < -300):
        print("game over")


        scoreboard.reset_scoreboard();
        snake.reset();

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) <10:
            print("Game over - collision with the snake's body");
            scoreboard.reset_scoreboard();
            snake.reset();
            print("Game over flag set to False");



screen.exitonclick()