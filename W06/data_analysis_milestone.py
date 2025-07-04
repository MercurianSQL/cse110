"""
Author: Marinda Keller
Purpose: to anaylize data using db files
"""


# Format
# Entity,Code,Year,Life expectancy (years)
# Afghanistan,AFG,1950,27.638
entity = ""
code = ""
year = 0
year = int(year)
life = 0.0
life = float(life)
lowest_life_expect = 100000.0
lowest_life_expect = float(lowest_life_expect)
highest_life_expect = 0.0
highest_life_expect = float(highest_life_expect)

with open("life-expectancy.csv") as life_expect_file: # Milestone 2
# with open("W06/life-expectancy.csv") as life_expect_file: # for my system use
    next(life_expect_file) 
    for line in life_expect_file:
                
        #Parsing Strings
        clean_line = line.strip()
#        print(clean_line) # Milestone 3:

        #Splitting a string into pieces   
        parts = clean_line.split(",")
        entity = parts[0].title()
        code = parts[1].upper()
        year = int(parts[2])
        life = float(parts[3]) 
#        print(f"{entity}, {code}, {year}, {life}") # Milestone 4:
        
        #Find lowest
        if life < lowest_life_expect:
            lowest_life_expect = life
            #print (f"The lowest life expectancy so far is {lowest_life_expect}.")
        if life > highest_life_expect:
            highest_life_expect = life
            #print (f"The highest life expectancy so far is {highest_life_expect}.")

    print(f"The lowest life expectancy ever was {lowest_life_expect} years.") # Milestone 5
    print (f"The highest life expectancy ever was {highest_life_expect} years.")
        #4)Keep track of the name of the person that is the youngest.
        #lowest_entity = entity


# Milestone Requirements:
# [x] Milestone 1: Download the dataset
# [x] Milestone 2: Load the dataset in your Python program
# [x] Milestone 3: Iterate through the data line by line  ## RESTART HERE!
# [x] Milestone 4: Split each line into parts
# [x] Milestone 5: Find the LOWEST value for life expectancy and the HIGHEST value for life expectancy in the dataset, and DISPLAY both values. 
# (Note that at this point, you just need the value for this, not the year and the country for that value.)
#
#  1)What is the year and country that has the lowest life expectancy in the dataset?
# Entity,Code,Year,Life expectancy (years)
# Afghanistan,AFG,1950,27.638


# 2)What is the year and country that has the highest life expectancy in the dataset?
# 3)Allow the user to type in a year, then, find the average life expectancy for that year. Then find the country with the minimum and the one with the maximum life expectancies for that year.

"""
life-expectancy.csv: 
Life Expectancy Data License
This dataset comes from: https://ourworldindata.org/spanish-flu-largest-influenza-pandemic-in-history

It is licensed under the Creative Commons BY license. You have the permission to use, distribute, and reproduce in any medium, provided the source and authors are credited.
The source information for the dataset is as follows:
Variable description: Life expectancy at birth is defined as the average number of years that a newborn could expect to live if he or she were to pass through life subject to the age-specific mortality rates of a given period.
Variable time span: 1543 – 2019
Data published by: James C. Riley (2005) – Estimates of Regional and Global Life Expectancy, 1800–2001. Issue Population and Development Review. Population and Development Review. Volume 31, Issue 3, pages 537–543, September 2005., Zijdeman, Richard; Ribeira da Silva, Filipa, 2015, "Life Expectancy at Birth (Total)", http://hdl.handle.net/10622/LKYT53, IISH Dataverse, V1, and UN Population Division (2019)
Data publisher's source: https://www.lifetable.de/RileyBib.pdf

Link: https://datasets.socialhistory.org/dataset.xhtml?persistentId=hdl:10622/LKYT53, http://onlinelibrary.wiley.com/doi/10.1111/j.1728-4457.2005.00083.x/epdf, https://population.un.org/wpp/Download/Standard/Population/ Data was compiled by Our World in Data based on estimates by James C. Riley, Clio Infra, and the United Nations Population Division.

For regional- and global-level data pre-1950, we use data from a study by Riley, which draws from over 700 sources to estimate life expectancy at birth from 1800 to 2001.
Riley estimated life expectancy before 1800, which he calls "the pre-health transition period". "Health transitions began in different countries in different periods, as early as the 1770s in Denmark and as late as the 1970s in some countries of sub-Saharan Africa". As such, for the sake of consistency, we have assigned the period before the health transition to the year 1770. "The life expectancy values employed are averages of estimates for the period before the beginning of the transitions for countries within that region. ... This period has presumably the weakest basis, the largest margin of error, and the simplest method of deriving an estimate."
For country-level data pre-1950, we use Clio Infra's dataset, compiled by Zijdeman and Ribeira da Silva (2015).
For country-, regional- and global-level data post-1950, we use data published by the United Nations Population Division, since they are updated every year. This is possible because Riley writes that "for 1950-2001, I have drawn life expectancy estimates chiefly from various sources provided by the United Nations, the World Bank’s World Development Indicators, and the Human Mortality Database".
For the Americas from 1950-2015, we took the population-weighted average of Northern America and Latin America and the Caribbean, using UN Population Division estimates of population size.
"""