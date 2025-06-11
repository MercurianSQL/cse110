"""
Author: Marinda Keller
Purpose: practice creating a Shopping Cart
"""

# creativity, options to purchase or return to shopping. Increased visibility of items in cart, cost of items in cart, and items removed from cart.



#starting options
five_action_main_menu = "Please select from one of the following options: \n1. Add item \n2. View cart \n3. Remove item \n4. Compute total \n5. Quit "
five_menu_actions = []
five_menu_actions = [1, 2, 3, 4, 5] # List to store action options of the main menu
five_menu_action = 0

# action 1 options: Add Item
input_item_name = "" # Variable to store the item name in concert with shopping_cart_items
input_item_price = 0.00 # Variable to STORE the item price in concert with shopping_cart_item_prices
shopping_cart_items = []  # List to store items in the shopping cart
shopping_cart_item_prices = []  # List to store prices of items in the shopping cart


#action 2 options: View Cart
iim_action = 0
iim_py_index = 0
#shopping_cart_items = ["bed", "blanket", "butter", "chair", "GF bread", "non-milk"] # for testing purposes

#shopping_cart_item_prices = [599.99, 29.99, 4.49, 349.99, 5.99, 5.49] # for testing purposes
input_item_name = "" # Variable to store the item name in shopping_cart
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
        print()
        print("These items are already in your cart: ")
        if len(shopping_cart_items) == 0:
            print("Your shopping cart is empty.")
        else:
            for i, input_item_name in enumerate(shopping_cart_items):
                print(f"{i+1}. {input_item_name}, ${shopping_cart_item_prices[i]:0.2f}")
        
        print()
        input_item_name = (input("What item would you like to add? "))
        if input_item_name == "0":
            five_menu_action = 0
        else:
            shopping_cart_items.append(input_item_name)
            input_item_price = float(input(f"What will you pay for {input_item_name}? "))
            shopping_cart_item_prices.append(input_item_price) 
            iim_action +=1
            iim_py_index = iim_action - 1
            print()
            #(shopping_cart_items) # for testing purpose
            #print(shopping_cart_item_prices) # for testing purpose
            print(f"Item {input_item_name}, ${input_item_price:0.02f} has been added to your cart.")
            five_menu_action = 0      


    elif five_menu_action == 2: #2. View cart
        print("Your Shopping Cart:")
        if len(shopping_cart_items) == 0:
            print("Your shopping cart is empty.")
            five_menu_action = 0
        for i, input_item_name in enumerate(shopping_cart_items):
            print(f"{i+1}. {input_item_name}, ${shopping_cart_item_prices[i]:0.2f}")
        for input_item_price in shopping_cart_item_prices:
            shopping_cart_subtotal += float(input_item_price)
        print(f"Your cart subtotal is ${shopping_cart_subtotal:0.2f}.")
        shopping_cart_subtotal = 0.00 # reset the subtotal to prevent overcharge
        five_menu_action = 0


    elif five_menu_action ==3: #3. Remove item
        print("Available items to remove: ")
        for i, input_item_name in enumerate(shopping_cart_items):
            print(f"{i+1}. {input_item_name}, ${shopping_cart_item_prices[i]:0.2f}")
        sci_action = i+1
        print("a")
        sci_action = int(input("Which item would you like to remove? "))
        sci_py_index = sci_action - 1
        # I cannot get this part working where it is supposed to check if the item to remove is within the list.
        # I will need to work on it in the morning when I can see it with fresh eyes. RESTART HERE!!
        #shopping_cart_length = int(len(shopping_cart_items))
        #print(0 <= sci_action, sci_py_index < shopping_cart_length) # for testing purposes
        # 0 less than sci_action or sci_py_index greater than length
        #while sci_action <=0 and sci_py_index > int(len(shopping_cart_items)):
        #    print("Invalid selection.")
        #    five_menu_action = 0
        #print("b")
        input_item_name = shopping_cart_items[sci_py_index]
        input_item_price = shopping_cart_item_prices[sci_py_index]
        print("c")
        shopping_cart_items.pop(sci_py_index)
        shopping_cart_item_prices.pop(sci_py_index)
        print(f"Item {sci_action}. {input_item_name}, ${input_item_price:0.02f} has been removed from your cart.")
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
                    shopping_cart_items = []  # List to store items in the shopping cart
                    shopping_cart_item_prices = []  # List to store prices of items in the shopping cart
                    five_menu_action = 0
                else:
                    print("Payment aborted.")
                    shopping_cart_subtotal = 0.00 # reset the subtotal to prevent overcharge
                    five_menu_action = 0
            else:
                shopping_cart_subtotal = 0.00 # reset the subtotal to prevent overcharge
                five_menu_action = 0

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
[x] Change the add functionality to also ask for and store the price of the item.
[x] Change the display functionality to also display the prices of the items.
[x] When displaying the items, display a number in front of each item. The numbers should start with 1.
[x] Complete the option to display the total amount of the prices of all the items in the shopping cart.
[x] Whenever prices are displayed, they should be shown to two decimal places and include the appropriate currency symbol (for example $, €, etc.)
[x] Complete the option to remove an item from the shopping cart.
[x] When removing an item, you should verify the following:
[x] Both the item name and price are removed from their respective lists.
[x] The number the user enters should be converted to a 0-based index 
[0] and checked to make sure it is within the bounds of the list.
[x] The program allows you to remove any item from the list including the first one and the last one. (Sometimes, if you have a bug in your project you might not allow removing the last item as you should.)

"""