import random
from tkinter import *
s = {
    "rock": {"rock": 1, "paper": 0, "scissor": 2},
    "paper": {"rock": 2, "paper": 1, "scissor": 0},
    "scissor": {"rock": 0, "paper": 2, "scissor": 1}
}

comp_score=0
player_score=0
total_rounds=0
current_round=0
def outcome_handler(user_choice):
    global comp_score, player_score, current_round
    outcomes = ["rock", "paper", "scissor"]
    random_number = random.randint(0, 2)
    computer_choice = outcomes[random_number]
    r = s[user_choice][computer_choice]
    player_choice_label.config(fg="red", text="Player Choice: " + str(user_choice))
    computer_choice_label.config(fg="green", text="Computer Choice: " + str(computer_choice))
    if r == 2:
        player_score += 1
        player_score_label.config(text="Player: " + str(player_score))
        outcome_label.config(fg="blue", text="Outcome: Player won")
    elif r == 1:
        comp_score += 1
        player_score += 1
        player_score_label.config(text="Player: " + str(player_score))
        computer_score_label.config(text="Computer: " + str(comp_score))
        outcome_label.config(fg="blue", text="Outcome: It's a tie")
    elif r == 0:
        comp_score += 1
        computer_score_label.config(text="Computer: " + str(comp_score))
        outcome_label.config(fg="blue", text="Outcome: Computer won")
    current_round += 1
    if current_round >= total_rounds:
        end_game()

def end_game():
    global comp_score, player_score, total_rounds, current_round
    player_score = 0
    comp_score = 0
    current_round = 0
    player_score_label.config(text="Player: 0")
    computer_score_label.config(text="Computer: 0")
    outcome_label.config(text="Game Over! Please start again.")

def start_game():
    global total_rounds
    total_rounds = int(rounds_entry.get())
    rounds_entry.config(state=DISABLED)
    play_button.config(state=DISABLED)

m = Tk()
m.title("RPS")
Label(m, text="Rock, Paper, Scissor", font=("calibri", 14)).grid(row=0, sticky=N, pady=10, padx=200)
Label(m, text="Please select an option ", font=("calibri", 12)).grid(row=1, sticky=N)
Label(m, text="Number of Rounds:", font=("calibri", 12)).grid(row=6, sticky=W, pady=5)
rounds_entry = Entry(m)
rounds_entry.grid(row=6,column=1,sticky=W,pady=5)
play_button = Button(m,text="Start Game",command=start_game)
play_button.grid(row=7,columnspan=2, pady=5)
player_score_label = Label(m,text="Player:0",font=("calibri", 12))
player_score_label.grid(row=2,sticky=W)
computer_score_label = Label(m,text="Computer: 0",font=("calibri", 12))
computer_score_label.grid(row=2, sticky=E)
player_choice_label = Label(m, font=("calibri",12))
player_choice_label.grid(row=3,sticky=W)
computer_choice_label = Label(m,font=("calibri",12))
computer_choice_label.grid(row=3,sticky=E)
outcome_label = Label(m, font=("calibri", 12))
outcome_label.grid(row=3, sticky=N)
Button(m,text="Rock", width=15, command=lambda: outcome_handler("rock")).grid(row=4, sticky=W, padx=5, pady=5)
Button(m,text="Paper", width=15, command=lambda: outcome_handler("paper")).grid(row=4, sticky=N, pady=5)
Button(m,text="Scissor", width=15, command=lambda: outcome_handler("scissor")).grid(row=4, sticky=E, padx=5, pady=5)
Label(m).grid(row=5)
m.mainloop()
