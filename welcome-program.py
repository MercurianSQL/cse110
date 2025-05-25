# print("Welcome to CSE110!")
# print()
# print("This is going to be a great course.")
# print("Variables")
# name = "bob"
# age = 24
# print (name)
# print (age)
# age = 34
# print (name)
# print (age)
# print ("F-stirng")
# print (f"Your name is {name}")
       
# print(f"Your age is {age}.")

# place = "Rexburg"
# print (f"You are from {place}.")
# place = input ("Where are you from? ")
# print()

# vacation_place = input ("Where do you want to go on vacation? ")
# print (f"You are from {place} and you want to go to {vacation_place} on vacation.")
# print (f"You are from {place} and you want to go to {vacation_place} on vacation.") 

# print ("Favorite Color")
# color = input ("What is your favorite color? ")
# print (f"Your favorite color is {color}.")


# email = input("What is your email address? ")
# print(email.lower())
# print(email)
# email = email.lower()

# book = input("WHat is the title of the book? ")
# print(book.upper())
# print(book.capitalize())
# print(book.title())
# print(f"The title is: {book.title()}")

# print ("James Bond")
# f_name = input("What is your first name? ")
# l_name = input("What is your last name? ")
# print(f"My name is {l_name}, {f_name } {l_name}.")

# print ("James Bond.title")
# f_name = input("What is your first name? ")
# l_name = input("What is your last name? ")
# print(f"My name is {l_name.title()}, {f_name.title()} {l_name.title()}.")

"""
Author: Marinda Keller
Purpose: Formatting Strings"""

print("ID Badge Generator")
print()
print("Please enter the following information:")
print()
F_name = input("First Name: ")
L_NAME = input("Last Name: ")
email = input("Email: ")
phone = input("Phone Number: ")
Job_Title = input("Job Title: ")
ID = input("ID Number: ")
print()
print("The ID Card is:")
print("-----------------------------")
print(f"{L_NAME.upper()}, {F_name.capitalize()}")
print(f"{Job_Title.title()}")
print(f"ID: {ID}")
print()
print(f"{email.lower()}")
print(f"{phone}")
print("-----------------------------")

