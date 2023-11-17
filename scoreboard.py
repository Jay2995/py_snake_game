from turtle import Turtle;

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__();
        self.score = 0;
        self.highs_score = 0;
        self.ht()
        self.goto(x=0, y=250)
        self.color("White");
        self.update_score();

    def update_score(self):
        self.clear()
        self.write(arg=f"SCORE: {self.score} High score: {self.highs_score} ",move=False, align="center", font=('Courier', 10, 'normal')); 

    def reset_scoreboard(self):
        if self.score > self.highs_score:
            self.highs_score = self.score;
        self.score = 0;
        self.update_score(); 

    def increase_score(self):
        self.score += 1;
        self.update_score();
