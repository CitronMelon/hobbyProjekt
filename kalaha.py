class bowl:
    def __init__(self):
        self.balls = 6
    def add_ball(self):
        self.balls += 1
    def pick_up(self):
        balls = self.balls
        self.balls = 0
        return balls
class kalaha:
    def __init__(self) -> None:
        self.bowls = [bowl() for i in range(14)]
        self.bowls[6].balls = 0
        self.bowls[13].balls = 0
        self.player_1_turn = True
    def game_over(self):
        for i in range(14):
            if i != 6 and i != 13:
                if self.bowls[i].balls != 0:
                    return False
        return True
    def get_winner(self):
        p1 = self.bowls[6].balls
        p2 = self.bowls[13].balls
        if p1 > p2:
            return "Player 1"
        elif p1 < p2:
            return "Player 2"
        else:
            return "Its a tie"
    def show(self):
        def row(content):
            row = "| |"
            for item in content: row += f"[{item}]"
            row += "| |"
            print(row)
        print("Player 1")
        print(" >  1  2  3  4  5  6  >")
        row([b.balls for b in self.bowls[0:6]])
        row([self.bowls[13].balls, " ", " ", " ", " " , self.bowls[6].balls])
        row([b.balls for b in self.bowls[12:6:-1]])
        print(" <  6  5  4  3  2  1  < ")
        print("Player 2")
    def turn(self):
        def p_turn(home, exempt):
            print(f"Player {home%6+1}´s turn")
            arg = int(input("choose a bowl between 1 and 6 :")) - 1
            balls = self.bowls[arg + home - 6].pick_up()
            while (not(arg in [0,1,2,3,4,5] and balls != 0)):
                arg = int(input("choose a bowl between 1 and 6 :")) - 1 
                balls = self.bowls[arg + home - 6].pick_up()
            curr = 0
            pos = (arg + home - 5 + curr)%14
            while (balls != 0):
                if pos != exempt:
                    self.bowls[pos].add_ball()
                    balls  -= 1
                curr += 1
                pos = (arg + home - 5 + curr)%14
            sum = 0
            for i in range(home-6, home):
                sum += self.bowls[i].balls
            if sum == 0:
                other = 0
                for i in range(exempt-6, exempt):
                    other += self.bowls[i].pick_up()
            elif (pos-1)%14 == home :
                self.show()
                p_turn(home, exempt)
            elif self.bowls[(pos-1)%14].balls == 1 and pos >= home - 6 and pos < home and curr >= 8:
                self.bowls[home].balls += self.bowls[12 -  (pos-1)%14].pick_up() + self.bowls[(pos-1)%14].pick_up()
        P1C = 6
        P2C = 13
        if self.player_1_turn : 
            p_turn(P1C, P2C)
        else:
            p_turn(P2C, P1C)
        self.player_1_turn = not self.player_1_turn
game = kalaha()
while(not game.game_over()):
    game.show()
    game.turn()
print(game.get_winner())