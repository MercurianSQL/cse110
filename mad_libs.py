# I added a second paragraph and five additional variables to enhance the story.
# I also experimented with printing parentheses to see if they would require a \ like quote marks do.
# Mad Libs
"""Author: Marinda Keller
Title: W01 Project: Clever Stories
Description: User is prompted to enter parts of speech to complete unknown sentances with 
the purpose of making the readers smile, laugh, or absolutely guffaw.
"""

print("Please enter the following: ")
print()
adj = input("adjective ") 
animal = input("animal ")
body_part = input("body part ")
celebration = input("celebration ")
ed_verb = input("verb ending in -ed ")
exclamation = input("exclamation ")
ing_verb = input("verb ending in -ing ")
fam_member = input("family member ")
verb1 = input("verb ")
verb2 = input("verb ")
verb3 = input("verb ")
print()
print("Your story is:")
print()
print ("The other day, I was really in trouble. It all started when I saw a very")
print(f"{adj.lower()} {animal.lower()} {verb3.lower()} down the hallway. \"{exclamation.capitalize()}\"! I yelled. But all")
print(f"I could think to do was to {verb2.lower()} over and over. Miraculously,")
print(f"that caused it to stop, but not before it tried to {verb1.lower()}")
print("right in front of my family.")
print()
print(f"This was unfortunate becauSe the {animal.lower()} was going to be a")
print(f"surprise for my {fam_member.lower()} for their {celebration.lower()}.")
print(f"\"{exclamation.capitalize()},\" my {fam_member.lower()} yelled (becasue yelling runs in the family),")
print(f"\"I clearly wanted two {adj.lower()} {ing_verb.lower()} {animal.lower()}s for my {celebration.lower()}!\"")
print(f"I {ed_verb.lower()} my {body_part.lower()}. And that's why I stopped getting my {animal.lower()}s from the internet.")