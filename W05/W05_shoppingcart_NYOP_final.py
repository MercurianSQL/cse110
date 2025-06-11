"""
Author: Marinda Keller
Purpose: practice creating a Shopping Cart
"""

# creativity, options to purchase or return to shopping.



#starting options
five_action_main_menu = "Please select from one of the following options: \n1. Add item \n2. View cart \n3. Remove item \n4. Compute total \n5. Quit "
five_menu_actions = []
five_menu_actions = [1, 2, 3, 4, 5] # List to store action options of the main menu
five_menu_action = 0

# action 1 options: Add Item
static_items_menu = ["bed", "blanket", "butter", "chair", "GF bread", "non-milk"] # 
sim_action = 0
sim_py_index = 0
static_item_name = "" # Variable to store the item name in concert with static_items_menu

input_item_prices= [599.99, 29.99, 4.49, 349.99, 5.99, 5.49]  # Prices for each alphabetical item
input_item_price = 0.00 # Variable to STORE the item price in concert with input_item_prices

#action 2 options: View Cart
shopping_cart_items = []  # List to store items in the shopping cart
#shopping_cart_items = ["bed", "blanket", "butter", "chair", "GF bread", "non-milk"] # for testing purposes
shopping_cart_item_prices = []  # List to store prices of items in the shopping cart
#shopping_cart_item_prices = [599.99, 29.99, 4.49, 349.99, 5.99, 5.49] # for testing purposes
shopping_cart_item = "" # Variable to store the item name in shopping_cart
#*** come back to this shopping_cart_item_price variable!
#input_item_price = 0.00 # Variable to RETRIEVE the item price in shopping_cart_item_prices
sci_action = 0
sci_py_index = 0

#action 3 options: Remove Item
shopping_cart_subtotal = 0.00 # Variable to store the total price of items in the shopping cart

#action 4 options: Compute total
sales_tax_rate = 0.06 # Local sales tax rate for Rexburg, ID (6%)
cart_taxed = 0.00 # Variable to store the $sales tax amount on the shopping_cart_subtotal
taxed_total = 0.00 # Variable to store the $sales tax added to the shopping_cart_subtotal


print("Welcome to Club Shopping Cart!")
print()
print(f"{five_action_main_menu}")
print()

five_menu_action = int(input("Please enter an action: "))
while five_menu_action != 5:
    if five_menu_action == 1: #1. Add item
        print("Available items include: ")
        for i, static_item_name in enumerate(static_items_menu):
            print(f"{i+1}. {static_item_name}, ${input_item_prices[i]}")
        
        print()
        print("Congratulations! You have a 'Name Your Own Price' coupon to use on every item in this order!")
        print()
        sim_action = int(input("Which item would you like to add? "))
        sim_py_index = sim_action - 1
        static_item_name = static_items_menu[sim_py_index]
        input_item_price = input_item_prices[sim_py_index]
        print()
        shopping_cart_items.append(static_item_name) 
        input_item_price = float(input(f"Name Your Price for {static_item_name}? "))
        print(input_item_prices) # for testing purpose
        input_item_prices[sim_py_index] = input_item_price
        print(input_item_prices) # for testing purpose
        shopping_cart_item_prices.append(input_item_price)
        print(f"Item {sim_action}. {static_item_name}, ${input_item_price:0.02f} has been added to your cart.")
        five_menu_action = 0
        
    elif five_menu_action == 2: #2. View cart
        print("Your Shopping Cart:")
        if len(shopping_cart_items) == 0:
            print("Your shopping cart is empty.")
            five_menu_action = 0
        for i, shopping_cart_item in enumerate(shopping_cart_items):
            print(f"{i+1}. {shopping_cart_item}, ${shopping_cart_item_prices[i]:0.2f}")
        for input_item_price in shopping_cart_item_prices:
            shopping_cart_subtotal += float(input_item_price)
        print(f"Your cart subtotal is ${shopping_cart_subtotal:0.2f}.")
        shopping_cart_subtotal = 0.00 # reset the subtotal to prevent overcharge
        five_menu_action = 0


    elif five_menu_action ==3: #3. Remove item
        print("Available items to remove: ")
        for i, shopping_cart_item in enumerate(shopping_cart_items):
            print(f"{i+1}. {shopping_cart_item}, ${shopping_cart_item_prices[i]:0.2f}")
        sci_action = i+1
        print()
        sci_action = int(input("Which item would you like to remove? "))
        sci_py_index = sci_action - 1
        shopping_cart_item = shopping_cart_items[sci_py_index]
        input_item_price = shopping_cart_item_prices[sci_py_index]
        print()
        shopping_cart_items.pop(sci_py_index)
        shopping_cart_item_prices.pop(sci_py_index)
        print(f"Item {sci_action}. {shopping_cart_item}, ${input_item_price:0.02f} has been removerd from your cart.")
        five_menu_action = 0

    elif five_menu_action == 4: #4. Compute total  # cost cost is messed up becasue of NYOP: correct!
        print("Your Shopping Cart:")
        if len(shopping_cart_items) == 0:
            print(f"Your shopping cart is empty. Total is ${input_item_price:0.2f}")
            five_menu_action = 0
        else: 
            #print(len(shopping_cart_items)) #testing 
            for input_item_price in shopping_cart_item_prices:
                shopping_cart_subtotal += float(input_item_price)
            print(f"Your cart subtotal is ${shopping_cart_subtotal:0.2f}.")
            purchase = input("Are you ready to buy the items in your cart? 1 for Yes, 0 for No: ")
            if purchase == "1":
                #creativity, option to purchase.
                print("Local sales tax for Rexburg, ID is 6%")
                cart_taxed = round(shopping_cart_subtotal * sales_tax_rate, 2)  # Calculate sales tax, rounded to 2 decimals
                print(f"Tax on your purchase of ${shopping_cart_subtotal:0.2f} is ${cart_taxed:0.2f}")
                taxed_total = round(shopping_cart_subtotal + cart_taxed, 2)
                print(f"The amount owed on this purchase is ${taxed_total:0.2f}.")
                if input("Can we charge the card on file? 1 for Yes, 0 for No: ") == "1":
                    print("Thank you for your purchase. Your items will arrive promptly.")
                    five_menu_action = 0
                else:
                    print("Payment aborted.")
                    shopping_cart_subtotal = 0.00 # reset the subtotal to prevent overcharge
                    print("Returning to Main Menu")
                    five_menu_action = 0
            else:
                shopping_cart_subtotal = 0.00 # reset the subtotal to prevent overcharge
                five_menu_action = 0

    else:
        print() 
        print("Returning to Main Menu") # 5. Quit
        print()
        print(f"{five_action_main_menu}")
        print()
        five_menu_action = int(input("Please enter an action: "))
print("Thank you. Goodbye.")

"""

milestone requirements:
[x] Have menu system that repeats until the user chooses quit.
[x] Create a list that will store the names of the items in the shopping cart.
[x] Complete the option to add the name of the item to the list. #1
[x] Complete the option to display the names of the items in the list. #2

Final requirements
[x] Store prices as well as names.
[] Change the add functionality to also ask for and store the price of the item.
[x] Change the display functionality to also display the prices of the items.
[x] When displaying the items, display a number in front of each item. The numbers should start with 1.
[x] Complete the option to display the total amount of the prices of all the items in the shopping cart.
[x] Whenever prices are displayed, they should be shown to two decimal places and include the appropriate currency symbol (for example $, €, etc.)
[x] Complete the option to remove an item from the shopping cart.
[x] When removing an item, you should verify the following:
[x] Both the item name and price are removed from their respective lists.
[x] The number the user enters should be converted to a 0-based index and checked to make sure it is within the bounds of the list.
[x] The program allows you to remove any item from the list including the first one and the last one. (Sometimes, if you have a bug in your project you might not allow removing the last item as you should.)

"""