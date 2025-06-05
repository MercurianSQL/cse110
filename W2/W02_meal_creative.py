"""
Author: Marinda Keller
Purpose: Calculate the complex total of a standard meal, for instance at a state fairground
"""
# Creativity signals: Added description, personality. Non-standard narrative structure. 
# Algebraic computation of sales tax and tip. Customers get to choose their own costs. 

cost_adult = 18.00
cost_child = 9.25
print ("Welcome to WhatsHot World Fair Foods!")
print()
print (f"Adult meals are ${cost_adult:.2f} each.")
print ("An adult meal includes an entrée, a large side, and a large drink.")
print()
print (f"Child meals are ${cost_child:.2f} each.")
print ("A child meal includes a half-size entrée, a small side, and a small drink.")
print()
print ("Our meal prices include the 12.03% local restaurant sales tax and a 20% tip for our hard-working staff.")
print ("Please place your order when you are ready.")
print()

# customer input section
qty_adult = int(input("How many Adult meals? "))
adult_meals_total = float(cost_adult * qty_adult)
print (f"{qty_adult} adult meals will be ${adult_meals_total:.2f}")
qty_child = int(input("How many Child meals? "))
child_meals_total = float(qty_child * cost_child)
print (f"{qty_child} child meals will be ${child_meals_total:.2f}")
meals_total = float(adult_meals_total + child_meals_total)
print (f"The total for your order is ${meals_total:.2f}")
print()

#creativity starts here...
print ("CONGRADULATIONS! You qualify for our Name-Your-Own-Price coupon.")
print("Remember, our meal prices include the 12.03% local restaurant sales tax and a 20% tip for our hard-working staff.")
print()
cost_adult = float(input("What is the price of an adult meal? $"))
cost_child = float(input("What is the price of a child meal? $"))
print (f"Now, your Adult meals each cost ${cost_adult:.2f} and your Child meals each cost ${cost_child:.2f}.")
adult_meals_total = float(cost_adult * qty_adult)
child_meals_total = float(qty_child * cost_child)
meals_total = float(adult_meals_total + child_meals_total)
print (f"The total for your order is ${meals_total:.2f}")
print()
print("Wait! There's more...")

#taxes
tax_rate = float(input("What is the local restaurant sales tax percentage? "))
print()
print (f"You said the local restaurant sales tax percentage is {tax_rate:.2f}%. Nice try.")
tax_rate = float(12.03)
print ("However, Uncle Sam doesn't take coupons.")
print()
print (f"The local restaurant sales tax percentage is {tax_rate:.2f}%.")

print (f"The total for your order is ${meals_total:.2f}")
actual_cost = 0.757404 * (meals_total)
tip_total = .2 * (actual_cost)
tax_total = meals_total - actual_cost - tip_total
print (f"The local restaurant sales taxes of {tax_rate:.2f}% being collected on the ${actual_cost:.2f} subtotal of your ${meals_total:.2f} order is ${tax_total:.2f}.")
print()

# tips
print (f"A 20% tip of ${tip_total:.2f} is being collected on your meal subtotal of ${actual_cost:.2f}.")
print (f"100% of your ${tip_total:.2f} tip is paid directly to the service employees at this location.")
print("Thank you for your patronage.")
print()
# payment
math_check= float(actual_cost + tax_total + tip_total)
print (f"Your subtotal ${actual_cost:.2f} added to the tax of ${tax_total:.2f} and to the tip for ${tip_total:.2f} comes to ${math_check:.2f}")
print (f"The total for your order is ${meals_total:.2f}")
payment = float(input("What is the payment amount? $"))
print (f"The payment amount is ${payment:.2f}.")
change = payment - meals_total
print (f"Your order for ${meals_total:.2f} deducted from your payment of ${payment:.2f} leaves you with change of ${change:.2f}.")
print ("Please take your change.")
print ("Thank you for your business. Enjoy your food, and please come again.")
print()