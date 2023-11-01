from turtle import Turtle;
from snake import random_colour;
import random;


class Food(Turtle):

    def __init__(self):
        super().__init__();
        self.shape("circle");
        self.penup();
        self.shapesize(stretch_len = 0.5, stretch_wid=0.5)
        color = random_colour()
        self.color(color);
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280);
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y);
        self.color(random_colour());