userinput = input("Do you want to order a pizza? ") #asks the user if they want to order a pizza
pizzaOrder = [] #creates an empty list for the pizza order

if userinput.upper() in ("NO", "Q"): #if the user inputs no or q, then it will exit the program
    from pizzaReceipt import generateReceipt
    generateReceipt(pizzaOrder)
    
else: #if the user inputs anything else, then it will ask them to order a pizza
    def Order():  #function to order a pizza
        sizes = ("S", "M", "L", "XL") #sizes of pizza
        pizzasize = input("Choose a size: S, M, L, or XL: ") #asks the user to choose a size

        while pizzasize.upper() not in sizes: #if the user inputs anything other than the sizes, then it will ask them to choose a size again
            pizzasize = input("Choose a size: S, M, L, or XL: ")

        sizes = pizzasize.upper() #makes the size uppercase, easier for the code to work with
        toppings = ("ONION", "TOMATO", "GREEN PEPPER", "MUSHROOM", "OLIVE", "SPINACH", "BROCCOLI", "PINEAPPLE", "HOT PEPPER", "PEPPERONI", "HAM", "BACON", "GROUND BEEF", "CHICKEN", "SAUSAGE") #valid toppings options
        pizzatoppings = [] #creates an empty list to store the toppings
        toppingchoice = ("") #creates an empty string to store the user input for the toppings. initialized now so the following while loop can run

        while (toppingchoice.upper() != "X"): #while the user does not input x, then it will ask them to choose a topping
            print('Type in one of our toppings to add it to your pizza. To see the list of toppings, enter "LIST". When you are done adding toppings, enter "X"') 
            toppingchoice = input("") #asks the user to choose a topping

            if (toppingchoice.upper() in toppings): #if the user inputs a valid topping, then it will add it to the list of toppings
                toppingchoice = toppingchoice.upper()
                print("Added {} to your pizza".format(toppingchoice))
                pizzatoppings.append(toppingchoice)

            elif (toppingchoice.upper() not in toppings and toppingchoice.upper() !="X" and toppingchoice.upper() != "LIST"): #if the user inputs anything other than a valid topping, then it will ask them to choose a topping again
                print("Invalid toppings, try again.")

            elif (toppingchoice.upper() == "LIST"): #if the user inputs list, then it will print the list of toppings
                print(toppings)

        pizza = (sizes, pizzatoppings) #creates a tuple of the size and toppings
        pizzaOrder.append(pizza) #adds the tuple containing the pizza order to the list of pizza orders
        again = input("Do you want to continue ordering? ") #asks the user if they want to order another pizza

        while (again.upper() not in ("NO", "Q")): #if the user inputs anything other than no or q, then it will ask them to order another pizza
            Order()
            exit()

        from pizzaReceipt import generateReceipt
        generateReceipt(pizzaOrder)

    Order() # if yes, calls the function to order another pizza

