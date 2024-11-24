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

This project uses three libraries: pandas, random, os and datetime
"""
# ---------------------------------------
# Code
# ---------------------------------------
def player_search():
    print("\nWelcome To Player Search\n Please Select The League in which your team is playing.")
    print("\n1. English Premier League\n 2. LaLiga\n 3. Serie A\n 4. Bundesliga\n5. Ligue 1 Uber Eats")
    league = input('\nType the corresponding number to select or Leave Empty for a random league: ')
    if league == '':
        league = rd.randint(1, 5)
    while True:
        if league == 1 or league == '1':
            premier_league()
        elif league == 2 or league == '2':
            laliga()
        elif league == 3 or league == '3':
            serie_a()
        elif league == 4 or league == '4':
            bundesliga()
        elif league == 5 or league == '5':
            ligue_un()
        else:
            print("Invalid Input")

def premier_league():
    print("English Premier League has been selected.")
    conf = input("Would you like to change your preference? (yes/no): ")
    while True:
        if conf.casefold() == 'yes':
            return None
        elif conf.casefold() == 'no':
            print("Please Select Your Team from the list below:")
            print("1. Arsenal ")
        else:
            print("Please enter a valid input.")
def laliga():
    pass
def bundesliga():
    pass
def serie_a():
    pass
def ligue_un():
    pass


def view_shortlist(inpt):
    """
    A pretty straightforward function which either opens up your shortlist or clears your shortlist
    :param inpt:
    :return Noting:
    """
    if inpt==1:
        os.open("Shortlist.json", os.O_RDONLY)
    elif inpt==2:
        conf = input("Are You Sure? (yes/no): ")
        if conf.casefold()=="yes":
            open("Shortlist.json", "w").close()
        elif conf.casefold()=="no":
            return None
        else:
            print("Please enter yes or no")
    elif inpt==3:
        exit()
    else:
        print("Please enter a valid Choice")

print("\n\nWelcome To Football Manager Scouting System\n\nWould You Like To:\n1. Search for a player" )
print("2. Manage Your Shortlist\n3. Exit this program\n")
while True:
    usr = input("Type the Corresponding number to enter your Choice: ")
    if usr == "1":
        player_search()
    elif usr == "2":
        srtlst = input("1. View Your Shortlist\n2. Reset Your Shortlist\n3. Exit this program\n")
        if os.path.exists("Shortlist.json"):
            view_shortlist(srtlst)
        else:
            print("Shortlist Doesn't Exist.")
    elif usr == "3":
        exit()
    else:
        print("Please input a valid choice")