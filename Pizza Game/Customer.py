"""
Version:                0.1 (Customer)
Date created:           27 September 2023
Date last worked on:    28 September 2023
Description:            Class for customers. This will be where each customer is created and used throughout the program.
Changes made:           -Created function getCustDict, was also completed.
                        -Function createCustomers was completed.
                        -Function givePreferences was completed.
Still to do:            -scorePizza function still needs to be created.
"""

import json
import random
import Kitchen

def getCustDict():
    # Open the customer json file containing all the customers and their pizza toppings. We store this in a dictionary to be used.
    with open("JSON/customers.json", "r") as cust_json:
        customerDict = json.load(cust_json)
    
    return customerDict

def createCustomer(customerDict):
    # List containing all the names of the customers to be used
    nameList = []
    for name in customerDict.keys():
        nameList.append(name)

    # Find a random customer and then create a class using that persons name
    randNumber = random.randrange(0,len(nameList))
    customerName = nameList[randNumber]

    toppings = customerDict.get(customerName)
    categories = Kitchen.getCategories(toppings)

    customer = clsCustomer(customerName, toppings, categories)

    return customer

class clsCustomer:
    def __init__(self, name, toppings, categories):
        self.custName = name
        self.custToppings = toppings
        self.custToppingsCategories = categories

    # Give the name of the customer as well as the toppings they want on their pizza.
    def givePreferences(self):
        return self.custName, self.custToppings
        

    # Take pizza and give it a score based on toppings chosen and customers preferance.
    def scorePizza(self, madePizza = [], madePizzaCategories = []):
        score = 0
        tempCustPizza = self.custToppings.copy()
        tempCustCategories = self.custToppingsCategories.copy()
        # Check for similar toppings
        for madePizzaTopping,madePizzaCategory in zip(madePizza.copy(), madePizzaCategories.copy()):
            # If the pizza topping is in the list of toppings that the customer wants.
            if madePizzaTopping in tempCustPizza:
                score += 3

                tempCustPizza.remove(madePizzaTopping)
                madePizza.remove(madePizzaTopping)
            # If the topping is not in the list
            elif madePizzaCategory in tempCustCategories:
                score += 1 

                tempCustCategories.remove(madePizzaCategory)
                madePizzaCategories.remove(madePizzaCategory)
                
                        
        return score