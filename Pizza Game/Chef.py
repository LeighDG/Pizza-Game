"""
Version:                0.1 (Chef)
Date created:           27 September 2023
Description:            Class for the chef(player). The chef class stores all the player choices and stats. 
"""

import Kitchen as Kitchen
from settings import clearConsole
class Chef:
    def __init__(self, name, score = 0):
        self.name = name
        self.score = score

    # Return the name of the chef
    def getName(self):
        return self.name

    # The player will make a choice from the list of toppings given from the kitchen.
    def chooseToppings(self, toppings, custName, preferenceToppings):
        topppingsChoicesList = ["","",""]

        # Loop for player to their choices of toppings.
        for i in range(0,3):
            # Keep asking until an appropiate choice is given.
            while True:
                clearConsole()
                # Story setup
                print(f"{custName} has walked into the store. The toppings they want on their pizza are:")
                
                # Print toppings
                for x in range(0,len(preferenceToppings)):
                    print(f"{str(x + 1)}. {preferenceToppings[x]}")
                

                # Shows list of the topping choices
                print("\nThe list of toppings to choose from is: ")
                for x in range(0,len(toppings)):
                    print(f"[{str(x + 1)}] {toppings[x]}")
                choice = 0
                try:
                    # Display the chosen toppings, but only after the first 
                    if i > 0:
                        print(f"\nCurrent toppings: {topppingsChoicesList}")

                    choice = int(input("\nPlease enter your topping choice: "))

                    # Verify the choice is in range
                    if choice in range(1, len(toppings) + 1):
                        topppingsChoicesList[i] = toppings.pop(choice - 1)
                        break
                    else:
                        clearConsole()
                        print("Please enter a number in the choice range!")
                        input("\nPress enter to continue!")
                        continue
                except:
                    clearConsole()
                    print("Please only enter the number of your choice!")
                    input("\nPress enter to continue!")
                    continue

        return topppingsChoicesList
    
    # Tally the chefs total score for all 5 customers
    def tallyScore(self,scoreForPizza):
        self.score += scoreForPizza

        return self.score
