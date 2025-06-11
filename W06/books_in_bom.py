"""
Author: Marinda Keller
Purpose: practice working with files and lists
"""
#opening files
with open("W06/books.txt") as books_file:

#reading data
    for file_line in books_file:
        #Parsing Strings
        clean_line = file_line.strip()
        #Splitting a string into pieces
        #words = sentence.split(" ")
        #iterate
        #for word in words:
            #print(word)
            #Header Lines
            #header_row = names_file.readline()   OR   next(names_file)
        print(clean_line)    