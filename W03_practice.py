"""
Author: Marinda Keller
Purpose: Practice if/else statements
"""

first = int(input("What is the first number? "))
second = int(input("What is the second number? "))
if first > second:
    print ("The first number is greater.")
else:
    print ("The first number is not greater.")
if first == second:
    print ("The numbers are equal.")
else:
    print ("The numbers are not equal")
if first < second:
    print ("The second number is greater.")
else:
    print ("The second number is not greater.")
print()
print()
animal= input("What is your favorite animal? ")
animal = animal.lower()
pug = "pug"
if animal == pug:
    print ("That's my favorite animal too!")
else:
    print ("That one is not my favorite.")


print ("Loaning money can be profitable or risky.") 
print ("To help us determine if you qualify for a loan, please") 
print ("rate your answer from 1 to 10 on each of the following conditions,")
print ("where 10 is high and 1 is low.") 
print()
large_loan = int(input("How large is the loan? "))
good_history = int(input("How good is your credit history? "))
high_income = int(input("How high is your income? "))
large_down = int(input("How large is your down payment? "))
print()
if large_loan >= 5:
    if good_history >= 7 and high_income >= 7:
        print ("Yes, you qualify for a loan.")
    elif good_history >= 7 or high_income >= 7:
        if large_down >= 5:
            print ("Yes, you qualify for a loan.")
        else: print ("You do not qualify for a loan at this time.")
    elif not good_history >= 7 and high_income >= 7:
        print ("You do not qualify for a loan at this time.")
elif not large_loan >= 5:
    if 4 > good_history:
        print ("You do not qualify for a loan at this time.")
    elif high_income >= 7 or large_down >= 7:
        print ("Yes, you qualify for a loan.")
    elif high_income >= 4 and large_down >= 4:
        print ("Yes, you qualify for a loan.")
    else: print ("You do not qualify for a loan at this time.")
else: print ("You do not qualify for a loan at this time.")
# In case there is a bug, you don't promise a loan you cannot extend.

x = 5

if x = 5:
    print("first")
else:
    print("second")