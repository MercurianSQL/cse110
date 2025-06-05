"""
Author: Marinda Keller
Purpose: Calculate the complex total of a standard meal, for instance at a state fairground
"""
# No creativity on Milestone assignment

cost_adult = 16.00
cost_child = 9.25
print ("Welcome to Whatnot World's Fair Foods!")
print (f"Adult meals are ${cost_adult:.2f} each.")
print (f"Child meals are ${cost_child:.2f} each.")
cost_adult = (float(input("What is the cost you will pay for an Adult meal? $")))
print (f"You will pay ${cost_adult:.2f} for each adult meal.")
cost_child = (float(input("What is the cost you will pay for a Child meal? $")))
print (f"You will pay ${cost_child:.2f} for each child meal.")
print ("Please place your order when you are ready.")
# customer input section
qty_adult = int(input("How many Adult meals? "))
adult_meals_total = float(cost_adult * qty_adult)
print (f"{qty_adult} adult meals will be ${adult_meals_total:.2f}")
qty_child = int(input("How many Child meals? "))
child_meals_total = float(qty_child * cost_child)
print (f"{qty_child} child meals will be ${child_meals_total:.2f}")
meals_total = float(adult_meals_total + child_meals_total)
print (f"The subtotal for your order is ${meals_total:.2f}")
print()
# taxes
tax_rate = float(input("What is the local restaurant sales tax percentage? "))
print (f"That is correct. The local restaurant sales tax percentage is {tax_rate}%.")
tax_total = float(meals_total * (tax_rate) * .01)
print(f"Tax on your order will be ${tax_total:.2f}")
order_total = (meals_total + tax_total)
print(f"The total of your order will be ${order_total:.2f}")
# payment
payment = float(input("What is the payment amount? $"))
print (f"The payment amount is ${payment:.2f}.")
change = payment - order_total
print (f"Your order for ${order_total:.2f} deducted from your payment of ${payment:.2f} leaves you with change of ${change:.2f}.")
print ("Thank you for your business. Enjoy your food, and please come again.")