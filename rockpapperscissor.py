"""
Simple Program with loops and conditional statements Using random module
"""
import random

user_score = 0
comp_score = 0
total_draw = 0
while True:
    print("\t <ROCK PAPER AND SCISSOR GAME>\n")

    choices = ["ROCK", "PAPER", "SCISSOR"]
    comp_action = random.choice(choices)
    user_action = None
    while user_action not in choices:
        user_action = input("Enter Rock, Paper Or Scissor : ").upper()

    print("Computer Action : ", comp_action)
    print("Your Action : ", user_action)
    if comp_action == user_action:
        print("RESULT :   GAME TIE!")
        total_draw += 1
    elif comp_action == 'SCISSOR':
        if user_action == "ROCK":
            print("RESULT :   WIN :)")
            user_score += 1
        else:
            print("RESULT :   LOSE :(")
            comp_score += 1
    elif comp_action == 'ROCK':
        if user_action == "PAPER":
            print("RESULT :   WIN :)")
            user_score += 1
        else:
            print("RESULT :   LOSE :(")
            comp_score += 1
    elif comp_action == 'PAPER':
        if user_action == "SCISSOR":
            print("RESULT :   WIN :)")
            user_score += 1
        else:
            print("RESULT :   LOSE :(")
            comp_score += 1

    x = input("Play again press Y else N : ").lower()
    if x != "y":
        break

print("Your Score : ", user_score)
print("Computer Score : ", comp_score)
print("Tie Matches : ", total_draw)
print("Game Exited")
