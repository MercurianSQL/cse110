"""
Name: Marinda Keller
Purpose: Learn and Practice functions
"""


def display_regular(message):
    """function prints a formatted message"""
    print(user_message_input)

def display_upper(message):
    """function prints a message in uppercase"""
    upper_user_message_input = user_message_input.upper()
    print(upper_user_message_input)

def display_lower(message):
    """function prints a message in lowercase"""
    lower_user_message_input = user_message_input.lower()
    print(lower_user_message_input)

#prompt user for the message
user_message_input = input("What is your message? ")

# print the message as typed
display_regular(user_message_input)
# print message in caps
display_upper(user_message_input)
# print message in lower
display_lower(user_message_input)