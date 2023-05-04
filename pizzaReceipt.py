def generateReceipt(pizzaOrder):
    total = 0

    if len (pizzaOrder) == 0: #if there is no order, then it will print that they did not order anything
        print("You did not order anything")

    else:
        print("Your order: ")
        for i in range(len(pizzaOrder)): #for loop runs in range of how many pizzas they order
            baseCost = 0 #base cost of pizza without extra toppings is set to 0 every time the loop runs
            extraToppings = 0 #extra toppings is set to 0 every time the loop runs
            extraToppingPrice = 0 #extra topping price is set to 0 every time the loop runs
            if pizzaOrder[i][0] == "S":
                extraToppingPrice = 0.50 #extra topping price is set to 0.50 if the pizza size is small
                baseCost = 7.99 #base cost of pizza is set to 7.99 if the pizza size is small
                total += 7.99 #total price of pizza is added to the total price of all pizzas
                if len (pizzaOrder[i][1]) > 3: #if there are more than 3 toppings, then it will calculate the added cost and number of extra toppings for later
                    total += (0.5* (len (pizzaOrder[i][1]) - 3))
                    extraToppings = len (pizzaOrder[i][1]) - 3

            elif pizzaOrder[i][0] == "M":
                extraToppingPrice = 0.75 #extra topping price is set to 0.75 if the pizza size is medium
                baseCost = 9.99 #base cost of pizza is set to 9.99 if the pizza size is medium
                total += 9.99  #total price of pizza is added to the total price of all pizzas
                if len (pizzaOrder[i][1]) > 3: #same function as small, but adjusted prices for additional toppings
                    total += (0.75* (len (pizzaOrder[i][1]) - 3))
                    extraToppings = len (pizzaOrder[i][1]) - 3

            elif pizzaOrder[i][0] == "L": 
                extraToppingPrice = 1.00 #extra topping price is set to 1.00 if the pizza size is large
                baseCost = 11.99 #base cost of pizza is set to 11.99 if the pizza size is large
                total += 11.99 #total price of pizza is added to the total price of all pizzas
                if len (pizzaOrder[i][1]) > 3: #same function as small, but adjusted prices for additional toppings
                    total += (1* (len (pizzaOrder[i][1]) - 3))
                    extraToppings = len (pizzaOrder[i][1]) - 3

            elif pizzaOrder[i][0] == "XL": 
                extraToppingPrice = 1.25 #extra topping price is set to 1.25 if the pizza size is extra large
                baseCost = 13.99 #base cost of pizza is set to 13.99 if the pizza size is extra large
                total += 13.99 #total price of pizza is added to the total price of all pizzas
                if len (pizzaOrder[i][1]) > 3: #same function as small, but adjusted prices for additional toppings
                    total += (1.25* (len (pizzaOrder[i][1]) - 3))
                    extraToppings = len (pizzaOrder[i][1]) - 3
                    
            print("Pizza " + str(i+1) + ": " + pizzaOrder[i][0] + "          " + str(baseCost)) #prints the size of the pizza and the base cost of the pizza

            for j in range(len(pizzaOrder[i][1])): #for loop runs in range of how many toppings they order
                print("- " + pizzaOrder[i][1][j], end = "\n") #prints the toppings they order
            for x in range(extraToppings): #for loop runs in range of how many extra toppings they order
                print("Extra Topping " + "(" + str(pizzaOrder[i][0] + ")" + "   {:.2f}".format(extraToppingPrice))) #prints how many times they ordered an extra topping and the price of the extra topping and the price added

        tax = total * 0.13 #calculates the tax
        total += tax  #adds the tax to the total price of the pizza
            
        print("Tax:                {:.2f}".format(tax)) #prints the tax
        print("Total:             {:.2f}".format(total)) #prints the total price of the pizza