"""
Author: Marinda Keller
Purpose: list practice


friends_list = []
friend = ""

while friend != "none":
    friend = input("Who is your friend? ")
    if friend != "none":
        friends_list.append(friend)
for friend in friends_list:
    print(friend)


Steps:
set variables
set the loop
gather input
correct the loop
end the loop
execute print list
"""

purchases = []
purchase = ""
remove = ""
replacement = ""

# User input 1
while purchase != "quit":
    purchase = input("Please enter the items of the shopping list (type: quit to finish): ")
    if purchase != "quit":
        purchases.append(purchase)
print()
# print list 1        
print("The shopping list is:")
for purchase in purchases:
    print(purchase)
print()  
# print list 2      
print("The shopping list with indexes is:")
for i in range(len(purchases)):
    purchase = purchases[i]
    print(f"{i}. {purchase}")
print() 
# User input 2  ***RESTART HERE*** stuck on getting place value and replacement to insert
remove = (int(input("Which item would you like to change? ")))
purchases.pop(remove)
replacement = input("What is the new item? ")
purchases.insert((remove), (replacement))
# Instructor used this code: and it does work. What was I overthinking?
# index = int(input("Which item would you like to change? "))
# new_item = input("What is the new item? ")
# shopping_list[index] = new_item
print() 
# print list 3
print("The shopping list with indexes is:")
for i in range(len(purchases)):
    purchase = purchases[i]
    print(f"{i}. {purchase}")

"""
Please enter the items of the shopping list (type: quit to finish):
Item: Milk
Item: Bread
Item: Candy
Item: Carrots
Item: quit


Which item would you like to change? 2
What is the new item? Apples

The shopping list with indexes is:
0. Milk
1. Bread
2. Apples
3. Carrots
"""