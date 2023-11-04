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
        self.write(arg=f"SCORE: {self.score}",move=False, align="center", font=('Courier', 10, 'normal')); 

    def game_over(self):
        # self.clear()
        self.goto(x=0, y=0);
        self.write(arg=f"GAME OVER. Your final score was {self.score}",move=False, align="center", font=('Courier', 15, 'normal')); 

