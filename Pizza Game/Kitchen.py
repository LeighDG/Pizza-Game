"""
Version:                0.1 (Kitchen)
Date created:           28 September 2023
Date last worked on:    28 September 2023
Description:            Class for the kitchen. The kitchen is responsible for allocating toppings for the chef and making the pizza.
Changes made:           -Kitchen class was made.
Still to do:            -giveToppings function needs to be made.
                        -makePizza function needs to be made
                        -AllToppings json file needs to be made.
"""
import json
import random

def getCategories(toppingOfGivenPizza):
    categories = []

    # Get the category that the topping is associated with.
    # Open alltoppings json to find out the category of the topping
    with open("JSON/alltoppings.json",'r') as toppings_obj:
        toppingsDict = json.load(toppings_obj)

    for pizzaTopping in toppingOfGivenPizza:  
        for category, toppings in toppingsDict.items():
            # Find the category that the pizza topping is in
            if pizzaTopping in toppings:
                categories.append(category)

    # Return the list
    return categories

def createKitchen():
    # Get all the toppings from the json file and create a kitchen class using them.
    with open("JSON/alltoppings.json","r") as topping_obj:
        allToppingsDict = json.load(topping_obj)

    # Get all the toppings from the dictionary and save them in a new list.
    allToppingsList = []
    for toppings in allToppingsDict.values():
        for topping in toppings:
            allToppingsList.append(topping)

    kitchen = clsKitchen(allToppingsList)

    return kitchen

class clsKitchen():
    # Initialize the kitchen class.
    def __init__(self, allToppings = []):
        self.allToppings = allToppings

    # Chooses random toppings from the alltoppings list and returns them in a new list.
    def giveToppings(self):
        tempList = self.allToppings.copy()
        chefToppings = ["","","","","",""]
        for i in range(0,6):
            randTopping = random.randrange(0,len(tempList))
            chefToppings[i] = tempList.pop(randTopping)

        return chefToppings
    
    # THe making of the pizza entails finding out the categories of the toppings on the pizza.
    def makePizza(self, playerToppings = []):
        categories = []
        categories = getCategories(playerToppings)

        return categories