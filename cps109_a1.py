import time
"""
A program which shows asks you for your budget to buy a house then asks what type of house do you want to buy and for
how many people it should be then displays recommended cities that would fit your budget after selecting the city you
like shows neighbourhoods with information such as crime index transit condition healthcare and basic facilities and
then asks which neighbourhood you would like and add it to a file which contains your selections
"""


"""
https://data.torontopolice.on.ca/datasets/TorontoPS::neighbourhood-crime-rates-open-data/explore?showTable=true
"""

"""
https://www.getwhatyouwant.ca/toronto-real-estate-prices-by-neighbourhood
"""

"""
Wellbeing Toronto
"""

"""
Divide the city in 4 sections:
Toronto
North York
Etobicoke 
Scarborough
"""

"""
Then divide each city into neighbourhood
"""

"""
Copyright Held by Jagrat Sharma 2024-10-30
© Jagrat Sharma
"""


"""
The problem will be that a person wantsto but a house but is too lazy to do any research so wants it to be done for him
"""

def main():
    """
    The main function of the program which manages all the print statements and inputs
    :return: Nothing
    """
    type_select()

def type_select():
    """
    Asks the use what kind of house they are looking for and based on their preference runs a seperate function
    :return: Nothing
    """
    while True:
        try:
            budget = int(input("What is your budget: $").lstrip())
        except ValueError:
            print()
            print("Please enter a valid number")
            print()
            time.sleep(2)
            continue
        print("What kind of house are you looking for?")
        print()
        print("1. Detached")
        print("2. Semi-Detached")
        print("3. Condos")
        print("4. Townhome")
        x = input("Input your preference: ").casefold()
        if x == "1" or x == "detached":
            detached(budget)
        elif x == "2" or x == "semi-detached":
            semi_detached(budget)
        elif x == "3" or x == "condos":
            condos(budget)
        elif x == "4" or x == "townhome":
            townhome(budget)
        elif x == "exit":
            print("Thank you for using My Program")
            break
        else:
            print("Please enter a valid preference")

def reader():
    """
    extracts information form the excel file and prints it out on the screen
    :return: Information from the excel file
    """
    pass
def writer():
    """
    writes the information to the excel file after the function is completed
    :return: Just a message saying data added to the excel file
    """
    pass
def money_range():
    """
    Chcks for money range with a infinite while loop and if/else statements
    :return: A value for the next function to operate on
    """
    pass
def detached(budget):
    pass
def semi_detached(budget):
    pass
def condos(budget):
    pass
def townhome(budget):
    pass
main()