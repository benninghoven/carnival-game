#from strip import Strip
#from mic import Mic
from screamer import Screamer

#s = Strip()
#s.Rainbow(10)
#s.Off()
#s.StartCountDown()

#exit()

"""
mic = Mic()
print("user 1 ")
print(mic.Listen())
"""

s = Screamer()
s.Play()

exit()


def UserStandBack(feet):
    print(f"telling user to stand back {feet} feet")

def PlayGame():
    while True:
        print("playing game")
        UserStandBack(5)
        break

def ViewLeaderboard():
    while True:
        print("viewing leaderboard")
        break

while True:
    userInput = input("1) Play Game\n2) View Leaderboard\n")
    if userInput == "1":
        PlayGame()
    elif userInput == "2":
        ViewLeaderboard()
    else:
        continue
