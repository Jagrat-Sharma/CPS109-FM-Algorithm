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
def team_select():
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
            print("1. Arsenal           6. Burnley          11. Ipswich          16. Norwich\n"
                  "2. Aston Villa       7. Chelsea          12. Liverpool        17. Nottm Forest\n"
                  "3. Bournemouth       8. Crystal Palace   13. Man City         18. Sunderland\n"
                  "4. Brentford         9. Everton          14. Man UFC          19. Tottenham\n"
                  "5. Brighton          10. Fullham         15. Newcastle        20. West Ham")
            team = input("Enter the corresponding number for the team or leave empty for : ")
            if team == '':
                team = str(rd.randint(1, 20))
            prem_player_search(team)
        else:
            print("Please enter a valid input.")
def laliga():
    print("LaLiga has been selected.")
    conf = input("Would you like to change your preference? (yes/no): ")
    while True:
        if conf.casefold() == 'yes':
            return None
        elif conf.casefold() == 'no':
            print("Please Select Your Team from the list below:")
            print("1. A.Bilbao              6. Cádiz          11. Las Palmas          16. Sevilla\n"
                  "2. A. Madrid             7. Espanyol       12. R. Madrid           17. Tenerife\n"
                  "3. Alavés                8. Getafe         13. Real Hispalis       18. Valencia\n"
                  "4. Atlético Pamplona     9. Girona         14. Real San Sebastián  19. Vallecano\n"
                  "5. Barcelona             10. Granada       15. S. Gijón            20. Villarreal")
        else:
            print("Please enter a valid input.")
def bundesliga():
    print("Bundesliga has been selected.")
    conf = input("Would you like to change your preference? (yes/no): ")
    while True:
        if conf.casefold() == 'yes':
            return None
        elif conf.casefold() == 'no':
            print("Please Select Your Team from the list below:")
            print("1. 1. FC Köln              6. Eintracht Frankfurt          11. Mainz 05           16. VfB Stuttgart\n"
                  "2. Augsburg                7. FC Bayern                    12. Nürnberg           17. VfL Bochum\n"
                  "3. Bayer 04                8. Heidenheim                   13. RB Leipzig         18. VfL Wolfsburg\n"
                  "4. Borussia Dortmund       9. Hertha BSC                   14. SC Freiburg\n"
                  "5. Borussia M'gladbach     10. HSV                         15. TSG Hoffenheim")
        else:
            print("Please enter a valid input.")
def serie_a():
    pass
def ligue_un():
    print("Ligue 1 Uber Eats has been selected.")
    conf = input("Would you like to change your preference? (yes/no): ")
    while True:
        if conf.casefold() == 'yes':
            return None
        elif conf.casefold() == 'no':
            print("Please Select Your Team from the list below:")
            print(
                "1. AJ Auxerre             6. FC Lorient          11. OGC Nice          16. Rennes\n"
                "2. AS Monaco              7. FC Nantes           12. OL                17. Strasbourg\n"
                "3. ASSE                   8. Havre AC            13. OM                18. Toulouse FC\n"
                "4. Bordeaux               9. LOSC                14. Paris SG\n"
                "5. Brest                  10. Montpellier        15. RC Lens")
        else:
            print("Please enter a valid input.")
def prem_player_search(team):
    player = pd.read_excel("Prem Def.xlsx")
    player.set_index("Club", inplace=True)
    name = player.set_index("Name", inplace=False)
    club_player = player.loc[team]
    club_player.set_index("UID", inplace=True)
    lst = []
    for i in club_player.index:
        lst.append(club_player.loc[i]['Name'])
    print("chose player")
    app = 1
    dct = {}
    for i in lst:
        print(app, ". ", i, sep='')
        dct[app] = i
        app += 1
    # print(dct)
    x = int(input("Enter Your Player: "))
    while True:
        try:
            player_name = dct[x]
        except KeyError:
            print("enter the correct number")
        else:
            break
    player_stats = name.loc[player_name]
    return player_stats
def find_replacement(player):
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
        team_select()
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