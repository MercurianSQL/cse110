"""
Author: Marinda Keller
Purpose: practice creating a Shopping Cart
"""

# creativity, ask for quantity.


shopping_cart = []  # List to store items in the shopping cart
shopping_subtotal = []  # List to store prices of items in the shopping cart
main_menu = ""
main_menu = "Please select from one of the following options: \n1. Add item \n2. View cart \n3. Remove item \n4. Compute total \n5. Quit "
menu_actions = []
menu_actions = [1, 2, 3, 4, 5]
action = ""
items_menu = ["bed", "blanket", "bread", "butter", "chair", "milk"] # alphabetical
items_price= [ 1.99, 2.99, 0.99, 1.49, 4.99, 3.49]  # Prices for each alphabetical item
i_menu_actions = [1, 2, 3, 4, 5, 6]  # Indexes for items_menu
item = ""
im_action = 0



print("Welcome to the Shopping Cart Program!")
print()
print(f"{main_menu}")
print()

action = int(input("Please enter an action: "))
while action != 5:
    if action == 1:
        print("Available items include: ")
        for i, item in enumerate(items_menu):
            print(f"{i+1}. {item}, ${items_price[i]}")
        im_action = i+1
        print()
        im_action = int(input("Which item would you like to add? "))
        py_index = im_action - 1
        item = items_menu[py_index]
        print()
        shopping_cart.append(item) 
        print(f"The {im_action}. {item} has been added to your cart.")
        action = 0
        
    elif action == 2: #2. View cart
        print("View of your Shopping Cart")
        for i, item in enumerate(shopping_cart):
            print(f"{i+1}. {item}")
            action = 0



    elif action ==3: #3. Remove item
        print("placeholder 3")
    elif action == 4: #4. Compute total
        print("placeholder 4")
    else: 
        print("Returning to Main Menu") # 5. Quit
        print(f"{main_menu}")
        print()
        action = int(input("Please enter an action: "))
print("Thank you. Goodbye.")

"""
    
    print("Please select one of the following options: ")
1. Add item
2. View cart
3. Remove item
4. Compute total
5. Quit
Please enter an action: 1
What item would you like to add? chair
'chair' has been added to the cart.

print("Please select one of the following options: ")
1. Add item
2. View cart
3. Remove item
4. Compute total
5. Quit
Please enter an action: 1
What item would you like to add? blanket
'blanket' has been added to the cart.

print("Please select one of the following options: ")
1. Add item
2. View cart
3. Remove item
4. Compute total
5. Quit
Please enter an action: 2
The contents of the shopping cart are:
bed
chair
blanket

print("Please select one of the following options: ")
1. Add item
2. View cart
3. Remove item
4. Compute total
5. Quit
Please enter an action: 5
Thank you. Goodbye.


"""

"""
milestone requirements:
[x] Have menu system that repeats until the user chooses quit.
[x] Create a list that will store the names of the items in the shopping cart.
[x] Complete the option to add the name of the item to the list. #1
[x] Complete the option to display the names of the items in the list. #2

Final requirements
[] Store prices as well as names.
[] Change the add functionality to also ask for and store the price of the item.
[] Change the display functionality to also display the prices of the items.
[] When displaying the items, display a number in front of each item. The numbers should start with 1.
[] Complete the option to display the total amount of the prices of all the items in the shopping cart.
[] Whenever prices are displayed, they should be shown to two decimal places and include the appropriate currency symbol (for example $, €, etc.)
[] Complete the option to remove an item from the shopping cart.
[] When removing an item, you should verify the following:
[] Both the item name and price are removed from their respective lists.
[] The number the user enters should be converted to a 0-based index and checked to make sure it is within the bounds of the list.
[] The program allows you to remove any item from the list including the first one and the last one. (Sometimes, if you have a bug in your project you might not allow removing the last item as you should.)

options menu:
1-Add a new item
2-Display the contents of the shopping cart
3-Remove an item (only needed for the final project deliverable)
4-Compute the total (only needed for the final project deliverable)
5-Quit"""