"""
Author: Marinda Keller
Purpose: practice creating a Shopping Cart
"""

# creativity, option to purchase.



#starting options
main_menu = "Please select from one of the following options: \n1. Add item \n2. View cart \n3. Remove item \n4. Compute total \n5. Quit "
menu_actions = []
menu_actions = [1, 2, 3, 4, 5] # List to store action options of the main menu
menu_action = 0
# action 1 options
items_menu = ["bed", "blanket", "butter", "chair", "GF bread", "non-milk"] # alphabetical
item_prices= [599.99, 29.99, 4.49, 349.99, 5.99, 5.49]  # Prices for each alphabetical item
i_menu_actions = [1, 2, 3, 4, 5, 6]  # Indexes for items_menu
item_name = "" # Variable to store the item name in concert with items_menu
item_cost = 0.00 # Variable to store the item price in concert with item_prices
im_action = 0
i_py_index = 0
#action 2 options
shopping_cart = []  # List to store items in the shopping cart
# shopping_cart = ["bed", "blanket", "butter", "chair", "GF bread", "non-milk"] - for testing purposes
shopping_subtotal = []  # List to store prices of items in the shopping cart
# shopping_subtotal = [599.99, 29.99, 4.49, 349.99, 5.99, 5.49] - for testing purposes
cart_item = "" # Variable to store the item name in shopping_cart
cart_cost = 0.00 # Variable to store the item price in shopping_subtotal
cm_action = 0
c_py_index = 0
#action 3 options
cart_subtotal = 0.00 # Variable to store the total price of items in the shopping cart
#action 4 options
sales_tax_rate = 0.06 # Local sales tax rate for Rexburg, ID (6%)
cart_taxed = 0.00 # Variable to store the $sales tax amount on the cart_subtotal
taxed_total = 0.00 # Variable to store the $sales tax added to the cart_subtotal


print("Welcome to Club Shopping Cart!")
print()
print(f"{main_menu}")
print()

action = int(input("Please enter an action: "))
while action != 5:
    if action == 1: #1. Add item
        print("Available items include: ")
        for i, item_name in enumerate(items_menu):
            print(f"{i+1}. {item_name}, ${item_prices[i]}")
        
        print()
        im_action = int(input("Which item would you like to add? "))
        i_py_index = im_action - 1
        item_name = items_menu[i_py_index]
        item_cost = item_prices[i_py_index]
        print()
        shopping_cart.append(item_name) 
        shopping_subtotal.append(item_cost)
        print(f"Item {im_action}. {item_name}, ${item_cost} has been added to your cart.")
        action = 0
        
    elif action == 2: #2. View cart
        print("Your Shopping Cart:")
        if len(shopping_cart) == 0:
            print("Your shopping cart is empty.")
            action = 0
        for i, cart_item in enumerate(shopping_cart):
            print(f"{i+1}. {cart_item}, ${shopping_subtotal[i]}")
            action = 0


    elif action ==3: #3. Remove item
        print("Available items to remove: ")
        for i, cart_item in enumerate(shopping_cart):
            print(f"{i+1}. {cart_item}, ${shopping_subtotal[i]}")
        cm_action = i+1
        print()
        cm_action = int(input("Which item would you like to remove? "))
        c_py_index = cm_action - 1
        cart_item = shopping_cart[c_py_index]
        cart_cost = shopping_subtotal[c_py_index]
        print()
        shopping_cart.pop(c_py_index)
        shopping_subtotal.pop(c_py_index)
        print(f"Item {cm_action}. {cart_item}, ${cart_cost} has been removerd from your cart.")
        action = 0

    elif action == 4: #4. Compute total
        print("Your Shopping Cart:")
        if len(shopping_cart) == 0:
            print(f"Your shopping cart is empty. Total is ${cart_cost:0.2f}")
            action = 0
        else: 
            for cart_cost in shopping_subtotal:
                cart_subtotal += float(cart_cost)
            print(f"Your cart subtotal is ${cart_subtotal}.")
            purchase = input("Are you ready to buy the items in your cart? 1 for Yes, 0 for No: ")
            if purchase == "1":
                #creativity, option to purchase.
                print("Local sales tax for Rexburg, ID is 6%")
                cart_taxed = round(cart_subtotal * sales_tax_rate, 2)  # Calculate sales tax, rounded to 2 decimals
                print(f"Tax on your purchase of ${cart_subtotal} is ${cart_taxed}")
                taxed_total = round(cart_subtotal + cart_taxed, 2)
                print(f"The amount owed on this purchase is ${taxed_total}.")
                if input("Can we charge the card on file? 1 for Yes, 0 for No: ") == "1":
                    print("Thank you for your purchase. Your items will arrive promptly.")
                    action = 0
                else:
                    print("Payment aborted.")
                    print("Returning to Main Menu")
                    action = 0
            else:
                action = 0

    else:
        print() 
        print("Returning to Main Menu") # 5. Quit
        print()
        print(f"{main_menu}")
        print()
        action = int(input("Please enter an action: "))
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