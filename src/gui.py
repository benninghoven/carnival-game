from guizero import App, Text, PushButton, Slider, TextBox, Picture, Box, ListBox
from screamer import *
import re

LOADING_TIME = 1

blurple = "#7289da"
spacegrey = "#2c2f33"
betangrey = "#99aab5"

#Keyboard
labels = ['q','w','e','r','t','y','u','i','o','p',
             'a','s','d','f','g','h','j','k','l',
             'z','x','c','v','b','n','m','<']

class GUI():

    def __init__(self):
        self.s = Screamer()
        self.s.StartUp()
        self.app = App(title="Carnival Game", height=480, width=800, bg=spacegrey)
        self.app.full_screen = True
        # MAIN MENU
        self.menuBox = Box(self.app)
        self.menuTitle = Text(self.menuBox, text = "screamer",size=150, font="Times New Roman", color=betangrey)
        self.startButton = PushButton(self.menuBox, text="start game", command=self.StartGame)
        self.startButton.bg = blurple
        self.leaderboardsButton= PushButton(self.menuBox, text="leaderboard", command=self.ShowLeaderboard)
        self.leaderboardsButton.bg = blurple
        self.exitButton = PushButton(self.menuBox, text="exit", command=self.Destroy)
        self.exitButton.bg = blurple
        self.menuBox.hide()
        self.menuBox.disable()
        # LEADERBOARD
        self.leaderboardBox = Box(self.app)
        self.leaderboardBox.text_size = 20
        self.menuTitle = Text(self.leaderboardBox, text = "leaderboard",size=120, font="Times New Roman", color="purple")
        self.showMenu = PushButton(self.leaderboardBox, text="Menu", command=self.ShowMenu)
        self.showMenu.bg = blurple
        self.listbox = ListBox(self.leaderboardBox, scrollbar=True, width="fill")
        self.listbox.text_color = betangrey
        self.listbox.bg = spacegrey
        self.leaderboardBox.hide()
        self.leaderboardBox.disable()
        # GAME
        self.gameBox = Box(self.app)

        self.namePlate = TextBox(self.gameBox, width= "fill", text="BOB")
        self.namePlate.set_text_color(self.namePlate, (30,30,30))
        self.namePlate.bg = (255,255,255)
        self.keyboardBox = Box(self.gameBox, layout="grid", align="bottom")
        self.playButton = PushButton(self.gameBox, text="Scream", command=self.s.Play)
        self.playButton.bg = blurple


        row = 0
        col = -1
        for i in range(0,len(labels)):
            col += 1
            c = labels[i]
            if c == 'a':
                row = 1
                col = 0
            elif c == 'z':
                row = 2
                col = 0
            button = PushButton(self.keyboardBox, command=self.InputChar, args=[c], text=c, grid=[col,row], width=4, height=4)
            button.bg = blurple

        self.menuButton = PushButton(self.gameBox, command=self.ShowMenu, text="Menu")
        self.menuButton.bg = blurple

        self.gameBox.hide()
        self.gameBox.disable()

        self.PressContinueButton = PushButton(self.app, text="touch to play", command=self.ShowMenu, height="fill",width="fill")
        self.PressContinueButton.bg = blurple
        self.PressContinueButton.text_color = spacegrey
        self.PressContinueButton.bg = (255,0,0)
        self.PressContinueButton.text_size = 30
        #self.loadingSplash = Picture(self.app, image="title-splash.png")
        #self.app.after(LOADING_TIME * 1000, self.CloseSplash)
        self.app.display()

    def InputChar(self,c = ""):
        if c == '<':
            self.namePlate.clear()
            return 
        self.namePlate.append(c)

    def ShowMenu(self):
        self.PressContinueButton.hide()
        self.PressContinueButton.disable()

        self.leaderboardBox.hide()
        self.leaderboardBox.disable()

        self.gameBox.hide()
        self.gameBox.disable()

        self.menuBox.enable()
        self.menuBox.show()


    #def CloseSplash(self):
    #    self.loadingSplash.destroy()
    #    self.PressToPlay


    def ShowLeaderboard(self):
        self.menuBox.hide()
        self.menuBox.disable()

        self.leaderboardBox.enable()
        self.leaderboardBox.show()
        self.listbox.clear()

        with open("stats.txt", "r") as f:
            playerList= f.readlines()

        playerList = [sub[ : -1] for sub in playerList]
        playerList.sort(key=lambda temp : list(
        map(int, re.findall(r'\d+', temp)))[0])
        playerList.reverse()

        for i in range(0, len(playerList)):
            print(playerList[i])
            self.listbox.insert(i, playerList[i])


    def Destroy(self):
        print("destroyed")
        exit()

    def StartGame(self):
        self.menuBox.disable()
        self.menuBox.hide()

        self.gameBox.enable()
        self.gameBox.show()




    def ViewLeaderboards(self):
        print("viewing leaderboards")

    def CloseSplash(self):
        self.loadingSplash.destroy()

    #title.show()
    #startButton.show()
    #leaderboardsButton.show()
    #exitButton.show()S

#g = GUI()
#keyboardBox = Box(app, layout="grid", grid=[1,0], align = "bottom")
