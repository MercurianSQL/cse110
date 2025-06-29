"""
Author: Marinda Keller
Purpose: to anaylize data using db files
"""

# Creativity Requirement:
# I'm including number of countries reporting in a year and over time 
# to better understand verasity of data for the time period being looked at. 

#count number of unique countries
#count number of unique years
#get average number of countries and life-s per year reported


entity = ""
code = ""
year = int(0)
life = float(0.0)
lowest_life_expect = float(100000.0)
highest_life_expect = float(0.0)
input_year = int(0)
input_year_data = []
input_life_expectancy_data = []
input_entity_data = []
years_life_total = float(0.0)
average_life_of_input = float(0.0)
max_input_entity = ""
max_input_life_expectancy = float(0.0)
min_input_entity = ""
min_input_life_expectancy = float(100000.0)
unique_countries = []
unique_years = []
total_countries = int(0)
total_years = int(0)
earliest_year = int(100000.0) 
latest_year = int(0.0) 


with open("life-expectancy.csv") as life_expect_file: # Milestone 2
#with open("W06/life-expectancy.csv") as life_expect_file: # for my system use
    input_year = int(input("Enter the year of interest: "))
    #input_year = input_year
    next(life_expect_file)
    for line in life_expect_file:

        #Parsing Strings
        clean_line = line.strip()
        #print(clean_line) # Milestone 3:

        #Splitting a string into pieces   
        parts = clean_line.split(",")
        entity = parts[0].title()
        code = parts[1].upper()
        year = int(parts[2])
        life = float(parts[3]) 
        #print(f"{entity}, {code}, {year}, {life}") # Milestone 4:
        
        #Creativity part 1
        if entity not in unique_countries:
            unique_countries.append(entity)
        
        #Creativity part 2
        if year not in unique_years:
            unique_years.append(year)

        #Find lowest
        if life < lowest_life_expect:
            lowest_life_expect = life
            #print (f"The lowest life expectancy so far is {lowest_life_expect}.")
            lowest_entity = entity
            lowest_year = year
        if life > highest_life_expect:
            highest_life_expect = life
            #print (f"The highest life expectancy so far is {highest_life_expect}.")
            highest_entity = entity
            highest_year = year

        # creativity 3
        if year < earliest_year:
            earliest_year = year
            #print (earliest_year) # for testing

        if latest_year < year:
            latest_year = year
            #print (latest_year) # for testing

        if year  == input_year:
            # list.append(variable)

            input_year_data.append(year)
            input_life_expectancy_data.append(life)
            input_entity_data.append(entity)
        #print(input_year_data) # for testing
        #print(input_life_expectancy_data) # for testing
        #print(input_entity_data) # for testing

            #look for max life of input yr
            if life > max_input_life_expectancy:
                max_input_life_expectancy = life
                max_input_entity = entity
            
            #look for min life of input yr
            if life < min_input_life_expectancy:
                min_input_life_expectancy = life
                min_input_entity = entity 

        #figure the AVERAGE life expect value for all entities
    for life in input_life_expectancy_data:
        years_life_total += life 

        number_of_entities = len(input_life_expectancy_data)
        average_life_of_input = years_life_total / number_of_entities

    #print(number_of_entities) # for testing
    #print(years_life_total) # for testing
    #print(unique_countries) #for testing
    total_countries = len(unique_countries)
    #print(total_countries) #for testing
    #print(unique_years) #for testing
    total_years = len(unique_years) #for testing
    #print(total_years) #for testing
    print()
    print(f"For the year {input_year}: ")
    print(f"The average life expectancy across all countries with data ({number_of_entities}) in {input_year} was {average_life_of_input:0.2f} years.") 
    print(f"The max life expectancy was in {max_input_entity} at {max_input_life_expectancy:0.2f} years.")
    print(f"The min life expectancy was in {min_input_entity} at {min_input_life_expectancy:0.2f} years.")
    print()
    print(f"This data set covers {total_years} years ({earliest_year} to {latest_year}) across {total_countries} reported countries.")
    print(f"The highest life expectancy ever was {highest_life_expect:0.2f} years in {highest_year} {highest_entity}.") # Requirement 2
    print(f"The lowest life expectancy ever was {lowest_life_expect:0.2f} years in {lowest_year} {lowest_entity}.") # Requirement 1

            


# Milestone Requirements:
# [x] Milestone 1: Download the dataset
# [x] Milestone 2: Load the dataset in your Python program
# [x] Milestone 3: Iterate through the data line by line  ## RESTART HERE!
# [x] Milestone 4: Split each line into parts
# [x] Milestone 5: Find the LOWEST value for life expectancy and the HIGHEST value for life expectancy in the dataset, and DISPLAY both values. 
# (Note that at this point, you just need the value for this, not the year and the country for that value.)

# Final Requirements
# [x] Requirement 1) What is the year and country that has the lowest life expectancy in the dataset?
# [x] Requirement 2) What is the year and country that has the highest life expectancy in the dataset?
# [x] Requirement 3) Allow the user to type in a year, then, find the average life expectancy for that year. 
# [x] 3b)Then find the country with the minimum and the one with the maximum life expectancies for that year.



# For the year 1959:
# The average life expectancy across all countries was 54.95
# The max life expectancy was in Norway with 73.49
# The min life expectancy was in Mali with 28.077
# The overall max life expectancy is: 86.751 from Monaco in 2019
# The overall min life expectancy is: 17.76 from Iceland in 1882




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