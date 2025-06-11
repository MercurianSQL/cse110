"""
Author: Marinda Keller
Purpose: working with files
"""
name = ""
id_number = 0
job_title = ""
salary = 0.0
#open file
#with open("W06/hr_system.txt") as hr_file: ## my computer folder # dont forget the ""
with open("hr_system.txt") as hr_file:
    header_row = hr_file.readline() #OR   next(hr_file)
    #print(header_row)
    
    #read lines of file
    for hr_line in hr_file:
        ## INSTRUCTOR did this: 
        # clean_line = hr_line.strip() instead of stripping /n from last variable. 
        # hr_info = clean_line.split(" ")
        ## it makes sense because in a real db, there might be random spaces. 
        ## note they strip the line before they split the line...
        ## I thought that would cause and error. Is why i striopped [3].
        ## but no error==no worries :) 
        #print(hr_line) #for testing
        
        #split lines in to variables
        hr_info = hr_line.split(" ")
        #print(hr_info) #for testing
        name = hr_info[0]
        id_number = int(hr_info[1])
        job_title = hr_info[2]
        salary = float(hr_info[3].strip())
        #print(f"{name} (ID: {id_number}), {job_title} - ${salary:0.2f}.")

        # enhansements
        # paycheck /24
        paycheck = round(salary/24, 2)
        #print(paycheck) # for testing
        
        # engineer bonus $1K
        if job_title == "Engineer":
        # alt: if job_title.lower() == "engineer":
            paycheck += 1000
            #print(paycheck) # for testing

        print(f"{name} (ID: {id_number}), {job_title} - ${paycheck:0.2f}.")
