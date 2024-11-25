import pandas as pd, random as rd, os
# ---------------------------------------
# Student Information
# ---------------------------------------
"""
Name: Jagrat Sharma
Student No.: 501329185
"""
# ---------------------------------------
# Problem Description
# ---------------------------------------
"""
This is a problem which happened to me not too long ago so I thought it could be a good project.

Suppose You are playing Football Manager, and it's the final few days of the January transfer window. Your team is in
good form could potentially win the league title, but suddenly you find out that one of your key defender is injured
and is out for the rest of the season. You know that he is one of the main pivots of your defensive line and without
him, you are going to struggle. As the transfer window is only open for the next few days even if you send all your
scouts, they won't be able to find a replacement in time. So you need to find a good defender who can replace your
injured defender and is currently in form.

So what this program does is it takes an .xlsx file containing the information of players from your Football Manager
save and based on the stats of your injured defender it finds a good replacement and writes them in a .txt or .xlsx 
file which acts as your shortlist.

This program is inspired by the movie 'Moneyball' and uses a similar approach to find replacement players.

This project uses three libraries: pandas, random and os
"""
# ---------------------------------------
# Code
# ---------------------------------------
def team_select():
    """
    The most basic search function of the program which prompts the user to pick a between 5 leagues and based on their
    input calls their respective functions,which makes it easier for the user to select their team.
    :return:
    """
    print("\nWelcome To Player Search\n Please Select The League in which your team is playing.")
    print("\n1. English Premier League\n 2. LaLiga\n 3. Serie A\n 4. Bundesliga\n5. Ligue 1 Uber Eats")
    while True:
        league = input('\nType the corresponding number to select or Leave Empty for a random league or type exit to exit: ')
        if league == '':
            league = rd.randint(1, 5)
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
        elif league == 'exit':
            exit()
        else:
            print("Invalid Input")
def premier_league():
    """
    This function is executed when the user selects Premier League. This function contains the names of all the teams
    currently in the league. This function prompts the use to select a team and based on their choice tells the next
    function the name of the league and the team selected b the user
    :return:
    """
    print("English Premier League has been selected.")
    disc = {
        1:"Arsenal",
        6:"Burnley",
        11:"Ipswich",
        16:"Norwich",
        2:"Aston Villa",
        7:"Chelsea",
        12:"Liverpool",
        17:"Nottm Forest",
        3:"Bournemouth",
        8:"Crystal Palace",
        13:"Man City",
        18:"Sunderland",
        4:"Brentford",
        9:"Everton",
        14:"Man UFC",
        19:"Tottenham",
        5:"Brighton",
        10:"Fullham",
        15:"Newcastle",
        20:"West Ham"
    } # A dictionary containing all the team names with their keys being their alphabetical position as numbers
    print("Please Select Your Team from the list below:")
    print("1. Arsenal           6. Burnley          11. Ipswich          16. Norwich\n"
          "2. Aston Villa       7. Chelsea          12. Liverpool        17. Nottm Forest\n"
          "3. Bournemouth       8. Crystal Palace   13. Man City         18. Sunderland\n"
          "4. Brentford         9. Everton          14. Man UFC          19. Tottenham\n"
          "5. Brighton          10. Fullham         15. Newcastle        20. West Ham")
    while True:
        team = input("Enter the corresponding number for the team or leave empty for a random team: ")
        if team == '':
            team = rd.randint(1, 20) # Picks a random number for if the user does not have knowledge of the game
        try:
            print("Selected Team is", disc[int(team)])
        except:
            print("Invalid Input")
        x, y = player_search(disc[int(team)], "Prem")
        fin_lst = find_replacement(x, y)
        write_to_file(fin_lst, y)
        print()
        print("Players Added to Shortlist.")
        exit()
def laliga():
    """
    The exact copy of premier_league() function with the exact same functions but only different team names
    :return:
    """
    print("LaLiga has been selected.")
    disc = {
        1:"A. Bilbao",
        6:"Cádiz",
        11:"Las Palmas",
        16:"Sevilla",
        2:"A. Madrid",
        7:"Espanyol",
        12:"R. Madrid",
        17:"Tenerife",
        3:"Alavés",
        8:"Getafe",
        13:"Real Hispalis",
        18:"Valencia",
        4:"Atlético Pamplona",
        9:"Girona",
        14:"Real San Sebastián",
        19:"Vallecano",
        5:"Barcelona",
        10:"Granada",
        15:"S. Gijón",
        20:"Villarreal"
    }
    print("Please Select Your Team from the list below:")
    print("1. A. Bilbao              6. Cádiz          11. Las Palmas          16. Sevilla\n"
          "2. A. Madrid             7. Espanyol       12. R. Madrid           17. Tenerife\n"
          "3. Alavés                8. Getafe         13. Real Hispalis       18. Valencia\n"
          "4. Atlético Pamplona     9. Girona         14. Real San Sebastián  19. Vallecano\n"
          "5. Barcelona             10. Granada       15. S. Gijón            20. Villarreal")
    while True:
        team = input("Enter the corresponding number for the team or leave empty for a random team: ")
        if team == '':
            team = rd.randint(1, 20)
        try:
            print("Selected Team is", disc[int(team)])
        except:
            print("Invalid Input")
        # else:
            # write_json(fin_lst)
        x, y = player_search(disc[int(team)], "LaLiga")
        fin_lst = find_replacement(x, y)
        write_to_file(fin_lst, y)
        print()
        print("Players Added to Shortlist.")
        exit()
def bundesliga():
    """
    The exact copy of premier_league() function with the exact same functions but only different team names
    :return:
    """
    disc = {
        1: "1. FC Köln",
        6: "Eintracht Frankfurt",
        11: "Mainz 05",
        16: "VfB Stuttgart",
        2: "Augsburg",
        7: "FC Bayern",
        12: "Nürnberg",
        17: "VfL Bochum",
        3: "Bayer 04",
        8: "Heidenheim",
        13: "RB Leipzig",
        18: "VfL Wolfsburg",
        4: "Borussia Dortmund",
        9: "Hertha BSC",
        14: "SC Freiburg",
        5: "Borussia M'gladbach",
        10: "HSV",
        15: "TSG Hoffenheim",
    }
    print("Bundesliga has been selected.")
    print("Please Select Your Team from the list below:")
    print("1. 1. FC Köln              6. Eintracht Frankfurt          11. Mainz 05           16. VfB Stuttgart\n"
          "2. Augsburg                7. FC Bayern                    12. Nürnberg           17. VfL Bochum\n"
          "3. Bayer 04                8. Heidenheim                   13. RB Leipzig         18. VfL Wolfsburg\n"
          "4. Borussia Dortmund       9. Hertha BSC                   14. SC Freiburg\n"
          "5. Borussia M'gladbach     10. HSV                         15. TSG Hoffenheim")
    while True:
        team = input("Enter the corresponding number for the team or leave empty for a random team: ")
        if team == '':
            team = rd.randint(1, 18)
        try:
            print("Selected Team is", disc[int(team)])
        except:
            print("Invalid Input")
        x, y = player_search(disc[int(team)], "Germany")
        fin_lst = find_replacement(x, y)
        write_to_file(fin_lst, y)
        print()
        print("Players Added to Shortlist.")
        exit()
def serie_a():
    """
    The exact copy of premier_league() function with the exact same functions but only different team names
    :return:
    """
    print("Serie A has been selected.")
    disc = {
        1: "AC Milan",
        6: "Cagliari",
        11: "Juventus",
        16: "Salento",
        2: "AS Roma",
        7: "Cremonese",
        12: "Lazio",
        17: "Salernitana",
        3: "Atalanta",
        8: "Fiorentina",
        13: "Parma",
        18: "Sassuolo",
        4: "Bologna",
        9: "Genoa",
        14: "Parthenope",
        19: "Torino",
        5: "Brianza",
        10: "Inter",
        15: "Reggiana",
        20: "Udinese"
    }
    print("Please Select Your Team from the list below:")
    print("1. AC Milan          6. Cagliari          11. Juventus          16. Salento\n"
          "2. AS Roma           7. Cremonese         12. Lazio             17. Salernitana\n"
          "3. Atalanta          8. Fiorentina        13. Parma             18. Sassuolo\n"
          "4. Bologna           9. Genoa             14. Parthenope        19. Torino\n"
          "5. Brianza           10. Inter            15. Reggiana          20. Udinese")
    while True:
        team = input("Enter the corresponding number for the team or leave empty for a random team: ")
        if team == '':
            team = rd.randint(1, 20)
        try:
            print("Selected Team is", disc[int(team)])
        except:
            print("Invalid Input")
        # else:
        # write_json(fin_lst)
        x, y = player_search(disc[int(team)], "Italy")
        fin_lst = find_replacement(x, y)
        write_to_file(fin_lst, y)
        print()
        print("Players Added to Shortlist.")
        exit()
def ligue_un():
    """
    The exact copy of premier_league() function with the exact same functions but only different team names
    :return:
    """
    disc = {
        1: "AJ Auxerre",
        6: "FC Lorient",
        11: "OGC Nice",
        16: "Rennes",
        2: "AS Monaco",
        7: "FC Nantes",
        12: "OL",
        17: "Strasbourg",
        3: "ASSE",
        8: "Havre AC",
        13: "OM",
        18: "Toulouse FC",
        4: "Bordeaux",
        9: "LOSC",
        14: "Paris SG",
        5: "Brest",
        10: "Montpellier",
        15: "RC Lens",
    }
    print("Ligue 1 Uber Eats has been selected.")
    print("Please Select Your Team from the list below:")
    print(
        "1. AJ Auxerre             6. FC Lorient          11. OGC Nice          16. Rennes\n"
        "2. AS Monaco              7. FC Nantes           12. OL                17. Strasbourg\n"
        "3. ASSE                   8. Havre AC            13. OM                18. Toulouse FC\n"
        "4. Bordeaux               9. LOSC                14. Paris SG\n"
        "5. Brest                  10. Montpellier        15. RC Lens")
    while True:
        team = input("Enter the corresponding number for the team or leave empty for a random team: ")
        if team == '':
            team = rd.randint(1, 18)
        try:
            print("Selected Team is", disc[int(team)])
        except:
            print("Invalid Input")
        x, y = player_search(disc[int(team)], "Fren")
        fin_lst = find_replacement(x, y)
        write_to_file(fin_lst, y)
        print()
        print("Players Added to Shortlist.")
        exit()
def player_search(team, league):
    """
    The Most important function of the program which uses pandas to cycle through the dataframe and display players of
    the selected team.
    :param team: The name of the team selected in the previous step of the program.
    :param league: The name of league selected in the previous step of the program.
    :return: The stats of the selected player and the name of that player.
    """
    # If/Elif Block which selects based on the league parameter which .xlsx file to read
    if league == "Prem":
        player = pd.read_excel("Prem Def.xlsx")
    elif league == "LaLiga":
        player = pd.read_excel("LaLiga_def.xlsx")
    elif league == "Fren":
        player = pd.read_excel("Ligue_une_def.xlsx")
    elif league == "Germany":
        player = pd.read_excel("Bundesliga def.xlsx")
    else:
        player = pd.read_excel("Serie A def.xlsx")
    player.set_index("Club", inplace=True) # Sets the Column "Club" as the index of the DataFrame
    name = player.set_index("Name", inplace=False)# Makes a new dataframe which has the column "Name" as it's index
    club_player = player.loc[team] # Makes a new dataframe which only contains the players who have their index as the team selected.
    club_player.set_index("UID", inplace=True) # Changes the index of the dataframe obtained above to unique ID
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
    return player_stats, player_name
def find_replacement(player, player_name):
    """
    The Second most important function of the program which takes two parameters and based on them cycle through all the
    available players and finds the players which beat the current injured player in at least 7 of the most important
    stats for a defender chosen by us
    :param player: Stats of the injured player
    :param player_name: Name of the injured
    :return: list containing the names of players who can be the replacements
    """
    fin_lst = []
    prem_player = pd.read_excel("Prem Def.xlsx")    #Reads the excel file cointaining the stats of premier league defenders
    #Reads the excel file for their respective leagues and combine them together to form a huge dataframe containing all players
    laliga_player = pd.read_excel("LaLiga_def.xlsx")
    bun_player = pd.read_excel("Bundesliga def.xlsx")
    frn_player = pd.read_excel("Ligue_une_def.xlsx")
    itly_player = pd.read_excel("Serie A def.xlsx")
    combine = pd.concat([prem_player, laliga_player, bun_player, frn_player, itly_player])
    combine.set_index("UID", inplace=True)
    combine.drop("Best Pos", axis='columns', inplace=True)
    total = 0 # Count which represents the number of players deemed as replacements for the  injured player
    for i in combine.index:
        sum = 0
        if (player["Mins"]*55/100) < combine.loc[i]["Mins"]: # Checks the amount of Minutes the player has played should be 55% of our injured player
            #Checks all the key stats and with a -5% margin if the player selected by the for loop outperforms our injured player adds one to sum value which acts a tracker
            # for in how many key stats is the selected player better than the injured one
            if (player["Tck/90"]*95/100) < combine.loc[i]["Tck/90"]:
                sum += 1
            if (player["Pres A/90"]*95/100) < combine.loc[i]["Pres A/90"]:
                sum += 1
            if (player["Poss Won/90"]*95/100) < combine.loc[i]["Poss Won/90"]:
                sum += 1
            if (player["Clr/90"]*95/100) < combine.loc[i]["Clr/90"]:
                sum += 1
            if (player["Poss Lost/90"]*95/100) > combine.loc[i]["Poss Lost/90"]:
                sum += 1
            if (player["Pas %"]*95/100) < combine.loc[i]["Pas %"]:
                sum += 1
            if (player["Int/90"]*95/100) < combine.loc[i]["Int/90"]:
                sum += 1
            if (player["Hdrs W/90"]*95/100) < combine.loc[i]["Hdrs W/90"]:
                sum += 1
            if (player["Blk/90"]*0.95) < (combine.loc[i]["Blk/90"]):
                sum += 1
            if (player["Shts Blckd/90"]*95/100) < combine.loc[i]["Shts Blckd/90"]:
                sum += 1
            if (player["K Tck"]/player["Mins"])<(combine.loc[i]["K Tck"]/player["Mins"]):
                sum += 1
        if sum >= 7:
            fin_lst.append(combine.loc[i]["Name"]) #Adds the players who are better in at least 7 stats to a list which is returned at the end of the function
            total += 1
    fin_lst.remove(player_name) # removes the player's own name from the list
    return fin_lst
def write_to_file(lst, pl):
    """
    A function which takes a parameter lst containing the names of players who have been determined they could
    replace our injured player and pl being the name of the injured player.This function writes the names, age club,
    transfer value, etc. of the players in lst to a .xlsx file with it's spreadsheet name being the name of the injured player.
    :param lst:
    :param pl:
    :return:
    """
    prem_player = pd.read_excel("Prem Def.xlsx")        #Reads the excel file cointaining the stats of premier league defenders
    laliga_player = pd.read_excel("LaLiga_def.xlsx")    #Reads the excel file cointaining the stats of Laliga defenders
    bun_player = pd.read_excel("Bundesliga def.xlsx")   #Reads the excel file cointaining the stats of Bundesliga defenders
    frn_player = pd.read_excel("Ligue_une_def.xlsx")    #Reads the excel file cointaining the stats of League one defenders
    itly_player = pd.read_excel("Serie A def.xlsx")     #Reads the excel file cointaining the stats of Serie Adefenders
    combine = pd.concat([prem_player, laliga_player, bun_player, frn_player, itly_player])  #Combines the five dataframes obtained above into a single one
    combine.drop("UID", axis='columns', inplace=True)   #Removes The UID Column
    combine.set_index("Name", inplace=True)     #Sets the Name Column As the index
    p= combine.loc[lst] #
    #Remove Unnecessary Columns that we don't neeed
    p.drop("Best Pos", axis='columns', inplace=True)
    p.drop("Pres A/90", axis='columns', inplace=True)
    p.drop("Tck/90", axis='columns', inplace=True)
    p.drop("Mins", axis='columns', inplace=True)
    p.drop("Tck R", axis='columns', inplace=True)
    p.drop("Poss Won/90", axis='columns', inplace=True)
    p.drop("Clr/90", axis='columns', inplace=True)
    p.drop("Poss Lost/90", axis='columns', inplace=True)
    p.drop("Hdrs W/90", axis='columns', inplace=True)
    p.drop("Blk/90", axis='columns', inplace=True)
    p.drop("Shts Blckd/90", axis='columns', inplace=True)
    p.drop("K Tck", axis='columns', inplace=True)
    p.drop("Pas %", axis='columns', inplace=True)
    p.drop("Int/90", axis='columns', inplace=True)
    # Writes the final dataframe to excel file
    p.to_excel("Shortlist.xlsx", sheet_name=pl)
def view_shortlist(inpt):
    """
    A pretty straightforward function which either opens up your shortlist or clears your shortlist
    :param inpt:
    :return Noting:
    """
    if inpt=='1':
        os.system("start EXCEL.EXE Shortlist.xlsx")
        exit()
    elif inpt=='2':
        conf = input("Are You Sure? (yes/no): ")
        if conf.casefold()=="yes":
            open("Shortlist.xlsx", "w").close()
            exit()
        elif conf.casefold()=="no":
            return None
        else:
            print("Please enter yes or no")
    elif inpt==3:
        exit()
    else:
        print("Please enter a valid Choice")
#Basic Greeting to the user
print("\n\nWelcome To Football Manager Scouting System\n\nWould You Like To:\n1. Search for a player" )
print("2. Manage Your Shortlist\n3. Exit this program\n")
while True:
    """
    A while loop that prompts the user to select a choice which starts the function
    """
    usr = input("Type the Corresponding number to enter your Choice: ")
    if usr == "1":
        team_select()
    elif usr == "2":
        print("How would you like to Manage theshortlist")
        srtlst = input("1. View Your Shortlist\n2. Reset Your Shortlist\n3. Exit this program\n: ")
        if os.path.exists("Shortlist.xlsx"):
            view_shortlist(srtlst)
        else:
            print("Shortlist Doesn't Exist.")
    elif usr == "3":
        exit()
    else:
        print("Please input a valid choice")