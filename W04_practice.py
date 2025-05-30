"""
Author: Marinda Keller
Purpose: Practice while loops"""

#exercise 1
number = -1 # This class treats 0 as a positive number, so start with -1.
while number < 0:
    number = (int(input("Please type a positive number: ")))
    if number < 1:
        print("Sorry, that is a negative number. Please try again.")
print(f"The number is: {number}")
print()
print()
#exercise 2
candy = "no" # best practice for non numbers is to set at ""
while candy != "yes":
    candy = input("May I have a piece of candy? ").lower()
print("Thank you.")

# activity 1
color = ""
colors = ["red", "blue", "green", "yellow"]
for color in colors:
    print(f"{color}") # no f and {} needed here. 
print()
# activity 2
for i in range(1, 9):
    print (i)
print()
# activity 3
for i in range(2, 22, 2): # example uses 21
    print (i)
print()

# Looping through strings
letter = ""
favorite = ""
word = "commitment"
favorite = input("What is your favorite letter? ").lower()
# for letter in (word): no () in example
for letter in word: 
    if letter == favorite:
        print("_", end="")
    else:
        print((letter), end="")    
print()
word = "book of mormon"
for letter in word: 
    if letter == favorite:
        print("_", end="")
    else:
        print((letter), end="")
# Step 1: for M capitialize - done
# Step 2 single line - done
# Step 3 output as _  - done
# step 4 reset letter as variable input. - passed

animal = "rabbit"
while animal == "dog":
   print("a")
   animal = "cat"
   print("b")
print("c")

animal = "dog"
while animal == "dog":
   print("a")
   animal = "cat"
   print("b")
print("c")

animal = "dog"
while animal != "dog":
   print("a")
   animal = "cat"
   print("b")
print("c")
value = 10
while value < 20:
   value = value + 1
print(value)
while value < 20:
   value = value + 1
print(value)


