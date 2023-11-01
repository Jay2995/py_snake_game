from turtle import Turtle;

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__();
        self.score = 0;
        self.ht()
        self.goto(x=0, y=250)
        self.color("White");
        self.update_score();

    def update_score(self):
        self.clear()
        self.write(arg=f"SCORE: {self.score}",move=False, align="center", font=('Arial', 10, 'normal')); 

