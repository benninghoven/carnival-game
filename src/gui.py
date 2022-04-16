from guizero import App, Text, TextBox, PushButton, Combo
from time import sleep
import re

def start_game():
    game.hide()
    leaderboard.hide()
    username.hide()

#def save_to_file():
    #MAKE THIS BITCH OPEN A FILE AND SAVE NAME IN IT
    #MAKE SURE NAME DOES NOT ALREADY EXIST

def counter():
    bitch.value = int(bitch.value) + 1

def show_leaderboard():
    leaderboard.hide()
    stats_file = open("stats.txt", "r")
    stats = stats_file.readlines()
    stats.sort(key=lambda temp : list(
        map(int, re.findall(r'\d+', temp)))[0])
    stats.reverse()
    first = Text(app, "1st - " + stats[0], color="#FFD700", bg="black")
    second = Text(app, "2nd - " + stats[1], color="#C0C0C0", bg="black")
    third = Text(app, "3rd - " + stats[2], color="#CD7F32", bg="black")
    stats_file.close()
    bitch = Text(app, text="0", visible=False)
    bitch.repeat(1000,counter)
    print(game.value)
    if game.value == 1 :
        first.hide()
        second.hide()
        third.hide()

"""
def add_name(new_name): #Add function that adds name to file
    #names_file = open("names.txt", "a")
    #names_file.write(new_name.value) 
    #names_file.close()
    print("ADD NAME STARTED")
    with open("names.txt", "r") as f:
         names = [line.strip() for line in f]
    # FIXME VET THE NAME HERE
    if new_name.value in names:
        print("NAME ALREADY EXIST")
        return

    with open("names.txt", "a") as f:
        f.write(new_name.value)
        print(f"wrote new name {new_name.value}")
    print("ADD NAME FINISHED")

"""    


def play_game():
    game.hide()
    leaderboard.hide()
    #new_name = TextBox(app)
    #add = PushButton(app, command=add_name(new_name), text="Add New Name")
    with open("names.txt", "r") as f:
        names = [line.strip() for line in f]
    namesDropDownMenu = Combo(app, options=names)
    begin = PushButton(app, command=start_game, text="Start Screaming")  
    




app = App(title="Throater")
welcome_message = Text(app, text="Scream at a bitch", size=40, font="Times New Roman", color="red") 
game = PushButton(app, command=play_game, text="Play game")
leaderboard = PushButton(app, command=show_leaderboard, text="Leaderboard")
#display_leaderboard = PushButton(app, command=show_leaderboard, text="Leaderboard")
app.display()
