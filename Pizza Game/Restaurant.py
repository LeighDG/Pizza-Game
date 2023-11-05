"""
Version:        0.1 (Restaurant)
Date:           27 September 2023
Description:    This module will hold the main game loop, as well as serve as a caller to link
                the modules. All main operations will take place in the restaurant.
"""
import json
import Customer as Customer
import Chef as Chef
import Kitchen as Kitchen
from time import sleep
from settings import clearConsole

# Start menu that serves the purpose of getting a player name and initializing the Chef class.
def startMenu():
    # Clear the system console and welcome to the restaurant
    clearConsole()
    print("""Welcome to the Restaurant!
    
You are the chef where your goal is to create a pizza
where the toppings match as close as possible to the
customers order!
          
Enter 'q' to quit to Main Menu now!""")
    flag = False
    
    # Keep asking for player name until a valid name is given
    while True:
        playerName = input("\nPlease enter player name: ")

        # Validate player name
        if len(playerName) < 3:
            if playerName == 'q':
                print("Quitting to Main Menu...")
                sleep(3)
                break
            else:
                print("Player name cannot be smaller than 3 characters!")
        else:
            # Create our chef(player) class
            chef_class = Chef.Chef(playerName)

            flag = True
            break

    return flag, chef_class

# Function that gets all the highscores from the highscore file and sorts them
def printHighscores():
    # Open json and store into a dictionary
    with open("JSON/highscores.json",'r') as score_obj:
        scoresDict = json.load(score_obj)
        
        highScoreDict = {}
        # For loop for the top 10 scores
        for highScorePosition in range(0,10):
            # Check that scoresDict is occupied 
            if len(scoresDict) == 0:
                break
            # Initialize variables
            highestScore = -1
            scoreName = ""
            
            # Get the highest score aswell as the position its in
            for playerName, scores in scoresDict.items():
                # Initialize variables
                tempScore = scores[0]
                tempPos = 0

                # Find the highest score
                for i in range(1, len(scores)):
                    if scores[i] > tempScore:
                        tempScore = scores[i]
                        tempPos = i
            
                # Determine if the users score is the highest of all the users
                if tempScore > highestScore:
                    highestScore = tempScore
                    scoreName = playerName
                    pos = tempPos
                elif tempScore == highestScore:
                    # Scores that are the same will be selected based on alphabetical order
                    if playerName < scoreName:
                        scoreName = playerName
                        pos = tempPos

            # Add the scores in order with their position into a dictionary    
            highScoreDict.update({highScorePosition + 1 : {scoreName : highestScore}})
            # Delete already added scores as to not have repeats
            del scoresDict[scoreName][pos]

            # Delete items in the dictionary that are empty
            for playerName, scores in scoresDict.copy().items():
                if len(scores) == 0:
                    del scoresDict[playerName]

   
    if len(highScoreDict) != 0:
         # Print out the highscores
        print("Current High Scores!!")
        print("---------------------\n")
        for position, scores in highScoreDict.items():
            for playerName, score in scores.items():
                print(f"[{position}] {playerName} : {str(score)}")
            
    else:
        print("There are currently no highscores set. Please play to set some!")


# Function that contains the main game loop. Serves the purpose of calling all the necessary functions.
def runGame():
    # Call start menu
    flag, chef_class = startMenu()

    if flag:
        # Get the customer dictionairy
        
        customerDict = Customer.getCustDict()

        # Initialize the kitchen class
        kitchen_cls = Kitchen.createKitchen()

        # Start the game loop with all the call functions
        gameLoopCounter = 0
        while gameLoopCounter < 3:
            customer_cls = Customer.createCustomer(customerDict)
            
            # Ask chef if they wish to make the pizza or not(loop until a pizza is made)
            while True:
                custName, custPreferenceDict = customer_cls.givePreferences()
                toppingsForPizza = chef_class.chooseToppings(kitchen_cls.giveToppings(),custName, custPreferenceDict)
                print(f"The current toppings on the pizza are: {toppingsForPizza}")

                # The "cooked" pizza is the categories of the pizza that was "made"
                if input("Do you want to make this pizza(y/n)?: ") == 'y':
                    cookedPizza = kitchen_cls.makePizza(toppingsForPizza)
                    break
            
            # Score the pizza
            scoreForPizza = customer_cls.scorePizza(toppingsForPizza, cookedPizza)

            clearConsole()
            print(f"The customer gave the pizza a score of {scoreForPizza} points!")
            print(f"Total score for the pizza is {chef_class.tallyScore(scoreForPizza)} points!")

            gameLoopCounter += 1

            if gameLoopCounter != 3:
                input("\nPress the enter key for next customer!")
            else:
                print(f"\nYour final score is: {chef_class.score} points!")
        

        if input("\nWould you like to save the score(y/n)? ") == 'y':
            
            # Load the scores into a dictionary
            with open("JSON/highscores.json",'r') as score_obj:
                allScores = json.load(score_obj)
                # Append the new score into the dictionary
                try:
                    allScores[chef_class.name].append(chef_class.score)
                except:
                    allScores[chef_class.name] = [chef_class.score]

            # Save the score in the json file with it sorted.
            with open("JSON/highscores.json",'w') as score_obj:
                json.dump(allScores, score_obj, sort_keys= True)
            
            print("Score saved!")

# Main function containing the main program loop.
def Main():
    mainLoop = True

    while mainLoop:
        clearConsole()

        print("""Main Menu

[1] Start new game
[2] Display highscores
[3] Quit
        """)
        
        choice = input("\nEnter option: ")
        
        match choice:
            case "1":
                clearConsole()
                runGame()
            case "2":
                clearConsole()
                printHighscores()
                input("\nPress enter to return to Main Menu!")
            case "3":
                clearConsole()
                print("Thank you for playing!!")
                sleep(1)
                mainLoop = False

Main()