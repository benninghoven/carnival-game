from guizero import * 
from time import sleep
import re
from screamer import Screamer

class Gui():
    def __init__(self):
        print("initing started")
        self.screamer = Screamer()
        self.app = App(title="Throater")
        self.app.full_screen=True
        welcome_message = Text(self.app, text="Screamer", size=40, font="Times New Roman", color="red") 
        self.game = PushButton(self.app, command=self.play_game, text="Play game")
        self.leaderboard = PushButton(self.app, command=self.show_leaderboard, text="Leaderboard")
        self.app.display()
        self.Lapp = App(title="Leaderboard")
        self.Lapp.full_screen=True
        self.curName = "Platypus"
        self.curScore = "1234"
        self.begin = PushButton(self.app, command=self.start_game, text="Start Screaming")  
        self.namesDropDownMenu = Combo(self.app, options=names)
        self.highScore = Text(self.app, text=self.curName + " - " + self.curScore, size=12)
        print("done initing")

    def start_game(self):
        self.game.hide()
        self.leaderboard.hide()
        nameScore = self.screamer.Play(self.namesDropDownMenu.value)
        self.curName = nameScore["name"]
        self.curScore = nameScore["score"]
        self.begin.hide()
        self.namesDropDownMenu.hide()
        self.highScore = Text(self.app, text=str(self.curName) + " - " + str(self.curScore), size=20, color="purple")

    def show_leaderboard(self):
        self.leaderboard.hide()
        stats_file = open("stats.txt", "r")
        stats = stats_file.readlines()
        stats.sort(key=lambda temp : list(
            map(int, re.findall(r'\d+', temp)))[0])
        stats.reverse()
        first = Text(self.Lapp, "1st - " + stats[0], color="#FFD700", bg="black")
        second = Text(self.Lapp, "2nd - " + stats[1], color="#C0C0C0", bg="black")
        third = Text(self.Lapp, "3rd - " + stats[2], color="#CD7F32", bg="black")
        stats_file.close()

    def play_game(self):
        self.game.hide()
        self.leaderboard.hide()
        with open("names.txt", "r") as f:
            names = [line.strip() for line in f]
        self.namesDropDownMenu = Combo(self.app, options=names)
        self.begin = PushButton(self.app, command=self.start_game, text="Start Screaming")  
