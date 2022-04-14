from guizero import App, Text, TextBox, PushButton

def say_name():
    welcome_message.value = username.value

#def save_to_file():
    #MAKE THIS BITCH OPEN A FILE AND SAVE NAME IN IT
    #MAKE SURE NAME DOES NOT ALREADY EXIST

#def show_leaderboard():
    #DISPLAY LEADERBAORD


app = App(title="Throater")
welcome_message = Text(app, text="Scream at a bitch", size=40, font="Times New Roman", color="red") 
username = TextBox(app)
update_text = PushButton(app, command=say_name, text="Play game")
#display_leaderboard = PushButton(app, command=show_leaderboard, text="Leaderboard")
app.display()
