from turtle import Turtle;
import random;

STARTING_POSITION = [(0,0), (-20,0), (-40,0)];
MOVE_DISTANCE = 20;
UP = 90;
DOWN = 270;
LEFT = 180;
RIGHT = 0;


def random_colour():
    color = "#{:06x}".format(random.randint(0, 0xFFFFFF));
    return color;


class Snake:
    def __init__(self):
        self.segments = [];
        self.color = random_colour();
        self.create_snake();
        self.head = self.segments[0];
        # self.speed = 0;

    

    def create_snake(self):
        for obj in STARTING_POSITION:
            self.add_segment(obj);


    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor();
            new_y = self.segments[seg_num - 1].ycor();
            self.segments[seg_num].goto(new_x, new_y);
        self.head.forward(MOVE_DISTANCE);
    
    

    def add_segment(self, obj):
            snake_starting_body = Turtle();
            snake_starting_body.color(self.color);
            snake_starting_body.shape("square");
            snake_starting_body.penup();
            snake_starting_body.goto(obj);
            self.segments.append(snake_starting_body);

    def extend(self):
        self.add_segment(self.segments[-1].position())
    
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
            
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN);
    
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT);
    
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT);