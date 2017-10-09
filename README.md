# Python
import random
class Game:
    def __init__(self):
        self.LINEos = 0
        self.TIMEq = 4
        self.TIMEm = 15


class Team1:
    def __init__(self):
        self.BALL = 0
        self.SCORE = 0
        self.RUN = 10
        self.PASS = 5
        self.BLOCK = 9
        self.SPECk = 7
        self.SPECkr = 8
        self.SPECfg = 3
        self.SPECp = 6
        self.COVERz = 8
        self.COVERm = 6
        self.RUNd = 6


class Team2:
    def __init__(self):
        self.BALL = 0
        self.SCORE = 0
        self.RUN = 5
        self.PASS = 10
        self.BLOCK = 7
        self.SPECk = 8
        self.SPECkr = 10
        self.SPECfg = 7
        self.SPECp = 5
        self.COVERz = 7
        self.COVERm = 8
        self.RUNd = 8


class Team3:
    def __init__(self):
        self.BALL = 0
        self.SCORE = 0
        self.RUN = 7
        self.PASS = 8
        self.BLOCK = 8
        self.SPECk = 8
        self.SPECkr = 10
        self.SPECfg = 7
        self.SPECp = 8
        self.COVERz = 5
        self.COVERm = 6
        self.RUNd = 7


class Team4:
    def __init__(self):
        self.BALL = 0
        self.SCORE = 0
        self.RUN = 6
        self.PASS = 6
        self.BLOCK = 6
        self.SPECk = 6
        self.SPECkr = 6
        self.SPECfg = 6
        self.SPECp = 6
        self.COVERz = 10
        self.COVERm = 10
        self.RUNd = 10


class TeamE:
    def __init__(self):
        self.BALL = 0
        self.SCORE = 0
        self.RUN = 5
        self.PASS = 5
        self.BLOCK = 5
        self.SPECk = 5
        self.SPECkr = 5
        self.SPECfg = 5
        self.SPECp = 5
        self.COVERz = 5
        self.COVERm = 5
        self.RUNd = 5


class TeamM:
    def __init__(self):
        self.BALL = 0
        self.SCORE = 0
        self.RUN = 8
        self.PASS = 8
        self.BLOCK = 7
        self.SPECk = 7
        self.SPECkr = 8
        self.SPECfg = 8
        self.SPECp = 7
        self.COVERz = 8
        self.COVERm = 8
        self.RUNd = 7


class TeamH:
    def __init__(self):
        self.BALL = 0
        self.SCORE = 0
        self.RUN = 10
        self.PASS = 10
        self.BLOCK = 10
        self.SPECk = 10
        self.SPECkr =10
        self.SPECfg = 10
        self.SPECp = 9
        self.COVERz = 10
        self.COVERm = 10
        self.RUNd = 10


Game = Game()
while True:
    a = int(input('1 or 2 player'))
    if a == 1:
        print('team 1')
        print('Overall = 77')
        print('Offence = 83')
        print('Defence = 67')
        print('Special teams = 60')
        print('')  # new line
        print('team 2')
        print('Overall = 75')
        print('Offence = 73')
        print('Defence = 77')
        print('Special teams = 75')
        print('')  # new line
        print('team 3')
        print('Overall = 74')
        print('Offence = 77')
        print('Defence = 60')
        print('Special teams = 85')
        print('')  # new line
        print('team 4')
        print('Overall = 73')
        print('Offence = 60')
        print('Defence = 100')
        print('Special teams = 60')
        b = int(input('what team do you want to be '))
        if b == 1:
            PLAYER1 = Team1()
            break
        elif b == 2:
            PLAYER1 = Team2()
            break
        elif b == 3:
            PLAYER1 = Team3()
            break
        elif b == 4:
            PLAYER1 = Team4()
            break
        else:
            print('INVALID')
    elif a == 2:
        print('NOT IMPLEMENTED YET')
while True:
    j = int(input('Difficulty = Easy(1) Medium(2) Hard(3) '))
    if j == 1:
        Bot = TeamE()
        break
    elif j == 2:
        Bot = TeamM()
        break
    elif j == 3:
        Bot = TeamH()
        break
if a == 1:
    c = random.randint(1, 2)
    d = int(input('Heads(1) or Tails(2) '))
    if c == d:
        f = int(input('You won the flip, Kick(1) or Receive(2)'))
        while True:
            if f == 1:
                g = int(input('Normal kick(1) squib kick(2) on sides kick(3)'))
                if g == 1:
                    h = 10 - Bot.SPECkr
                    i = random.randint(0, 50)
                    if i < h:
                        PLAYER1.BALL += 1
                        Game.LINEos = 100 - (40 + (PLAYER1.SPECk * 5))
                    elif i > h:
                        Bot.BALL += 1
                        Game.LINEos = 40 + (PLAYER1.SPECk * 5)
                        if Game.LINEos == 100:
                            Game.LINEos = 20
                        elif Game.LINEos < 100:
                            k = random.randint(0, 6)
                            if k == 6:
                                k = random.randint(0, 6)
                                if k == 6:
                                    Game.LINEos = 0
                                else:
                                    Game.LINEos -= Bot.SPECkr * k + 30 + random.randint(-4, 4)
                            else:
                                Game.LINEos -= Bot.SPECkr * k + random.randint(-4, 4)
            if Game.LINEos <= 0:
                if PLAYER1.BALL == 1:
                    PLAYER1.BALL -= 1


