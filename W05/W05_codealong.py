"""
Author: Marinda Keller
Purpose: Code along for W05
"""
#numbers_listo = [18, 36, 2, 48, 6, 12, 9]
numbers_listo = []
entries = 0
entry = -1
sum_listo = 0
largest = 0
smallest = 100

print("Enter a list of numbers, type 0 when finished.")
while entry != 0:
    entry = int(input("Enter a number: "))
    numbers_listo.append(entry)
    
if entry == 0:
    for entry in numbers_listo:
        sum_listo += entry
    print(f"The sum is: {sum_listo}")

    numbers_listo.pop()
    entries = (len(numbers_listo))
    listo_average = sum_listo / entries
    print(f"The average is: {listo_average}")
    #zero is being added to the list, get it to stop.

    for entry in numbers_listo:
        if entry > largest:
            largest = entry
    print(f"The largest is {largest}")

    for entry in numbers_listo:
        if entry > 0 and smallest != 1:
            smallest = entry
        else:
            smallest == 1
    print(f"The smallest positive number is: {smallest}")

