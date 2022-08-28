"""
GUI BASED ROCK PAPER SCISSOR GAME
USING TKINTER for GUI window
AND PIL for operations on image
"""
import random
import tkinter
from PIL import Image, ImageTk

# Main Window
window = tkinter.Tk()
window.title("ROCKPAPERSCISSOR BY Akant")
window.configure(background="#000000")
# window.geometry("800x400")

# loading Pictures
rock_img_user = ImageTk.PhotoImage(Image.open("rock_user.png"))
paper_img_user = ImageTk.PhotoImage(Image.open("paper_user.png"))
scissor_img_user = ImageTk.PhotoImage(Image.open("scissor_user.png"))
rock_img_comp = ImageTk.PhotoImage(Image.open("rock_comp.png"))
paper_img_comp = ImageTk.PhotoImage(Image.open("paper_comp.png"))
scissor_img_comp = ImageTk.PhotoImage(Image.open("scissor_comp.png"))

# Insert pictures in our main window
user_image = tkinter.Label(window, image=rock_img_user, bg="#000000")
comp_image = tkinter.Label(window, image=rock_img_comp, bg="#000000")
comp_image.grid(row=1, column=0)
user_image.grid(row=1, column=4)

# Inserting Score Text
user_score = tkinter.Label(window, text=0, font=100, bg="#000000", fg="#fff")
comp_score = tkinter.Label(window, text=0, font=100, bg="#000000", fg="#fff")
user_score.grid(row=1, column=3)
comp_score.grid(row=1, column=1)

# Inserting indicator text
comp_text = tkinter.Label(window, text="COMPUTER", font=100, bg="#000000", fg="#fff")
user_text = tkinter.Label(window, text="AKANT", font=100, bg="#000000", fg="#fff")
comp_text.grid(row=0, column=1)
user_text.grid(row=0, column=3)

# Inserting Buttons
rock_button = tkinter.Button(window, text="ROCK", height=2, width=20, bg="red", fg="white",
                             command=lambda: updateimages("rock"))
rock_button.grid(row=2, column=1)
paper_button = tkinter.Button(window, text="PAPER", height=2, width=20, bg="green", fg="white",
                              command=lambda: updateimages("paper"))
paper_button.grid(row=2, column=2)
scissor_button = tkinter.Button(window, text="SCISSOR", height=2, width=20, bg="blue", fg="white",
                                command=lambda: updateimages("scissor"))
scissor_button.grid(row=2, column=3)

# Update Images of User and Computer by clicking on Buttons

choices = ["rock", "paper", "scissor"]


def updateimages(userinput):
    # for computer image change
    comp_input = random.choice(choices)
    if comp_input == "rock":
        comp_image.configure(image=rock_img_comp)
    elif comp_input == "paper":
        comp_image.configure(image=paper_img_comp)
    else:
        comp_image.configure(image=scissor_img_comp)

    # for user image change
    if userinput == "rock":
        user_image.configure(image=rock_img_user)
    elif userinput == "paper":
        user_image.configure(image=paper_img_user)
    else:
        user_image.configure(image=scissor_img_user)

    checkrpsresult(userinput, comp_input)


# Inserting Result Text
result_text = tkinter.Label(window, text="CLICK BUTTON ", font=300, bg="#000000", fg="#fff")
result_text.grid(row=3, column=2)


# Check Results Condition funciton
def checkrpsresult(user_action, comp_action):
    if comp_action == user_action:
        result_text['text'] = "Match Draw"
    elif comp_action == 'scissor':
        if user_action == "rock":
            result_text['text'] = "YOU WON!"
            user_score['text'] += 1
        else:
            result_text['text'] = "YOU LOSE!"
            comp_score['text'] += 1
    elif comp_action == 'rock':
        if user_action == "paper":
            result_text['text'] = "YOU WON!"
            user_score['text'] += 1
        else:
            result_text['text'] = "YOU LOSE!"
            comp_score['text'] += 1
    elif comp_action == 'paper':
        if user_action == "scissor":
            result_text['text'] = "YOU WON!"
            user_score['text'] += 1
        else:
            result_text['text'] = "YOU LOSE!"
            comp_score['text'] += 1


# For Run the GUI Window in a loop
window.mainloop()
