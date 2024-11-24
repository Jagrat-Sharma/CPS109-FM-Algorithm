import pandas as pd
import datetime as dt
import random as rd
import os
# ---------------------------------------
# Problem Description
# ---------------------------------------
"""
This is a problem which happened to me a while ago so I thought it could be a good project.

Suppose You are playing Football Manager, and it's the final few days of the January transfer window. Your team is in
good form could potentially win the league title, but suddenly you find out that one of your key defender is injured
and is out for the rest of the season. You know that he is one of the main pivots of your defensive line and without
him, you are going to struggle. As the transfer window is only open for the next few days even if you send all your
scouts, they won't be able to find a replacement in time. So you need to find a good defender who can replace your
injured defender and is currently in form.

So what this program does is it takes an .xlsx file containing the information of players from your Football Manager
save and based on the stats of your injured defender it finds a good replacement while taking into account their age
 and writes them in a json file which acts as your shortlist.

This approach is inspired by the movie 'Moneyball' and uses a similar approach to find replacement players.

This project uses three libraries: pandas, random and datetime
"""
# ---------------------------------------
# Code
# ---------------------------------------
def player_search():
    pass


def view_shortlist():
    if os.path.exists(file):
        pass
    else:
        pass


print("\n\nWelcome To Football Manager Scouting System\n\nWould You Like To:\n1. Search for a player" )
print("2. View Your Shortlist\n3. Exit this program")
while True:
    usr = input("Enter Your Choice: ")
    if usr == "1":
        player_search()
    elif usr == "2":
        view_shortlist()
    elif usr == "3":
        exit()
    else:
        print("Please input a valid choice")