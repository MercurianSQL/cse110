"""
Author: Marinda Keller
Purpose: Write a program to find the youngest person in the list.
"""
people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]
youngest_person = ""
youngest_so_far = 1000

#1)Iterate through the list and display each string to the screen.
for person_line in people:
    print(f"{person_line}")

print()
    #2)Split the string into a name and age and print them to the screen.
for person_line in people:
    person_info = person_line.split(" ")
    # This is how the instructor coded this part:
    ## parts = person_line.split() ## by default this will split on the space
        ## Set variables for the two different parts
    ## name = parts[0]
    ## age = int(parts[1])
    # Notice they were able to int the age right away.
    person_name = person_info[0]
    person_age = person_info[1] 
    print(f"{person_name} is age {person_age}.")

print()
    #3)Find the age that is the youngest. 
for person_line in people:
    person_info = person_line.split(" ")
    person_name = person_info[0]
    person_age = person_info[1] 
    age_int = int(person_age)
    if age_int < youngest_so_far:
        youngest_so_far = age_int        
        #4)Keep track of the name of the person that is the youngest.
        youngest_person = person_name
    print(f"The youngest person {youngest_person} is only age {youngest_so_far}.")
