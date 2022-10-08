# Name - Ryan Alumkal
# Grade - 11
# Description - Asks user for marks, caluclautes average mark, and displays the lowest and highest mark
# Date - Tuesday March 8th

#Initializing
total_mark = 0
lowest_mark = 100 
highest_mark = 0

#Asks user for the number of marks 
submissions = int(input("How many marks are there: "))

#For Loop
for i in range (submissions):
    mark = int(input("What is your mark: "))#Asks user for mark
   
    if mark < 0 or mark > 100: #If mark is invalid 
        while True: #While this condition is true 
            if mark < 0 or mark > 100: #If mark is invalid 
                mark = int(input("You entered a mark that is not between 0 and 100. The calculate average may not make sense: ")) #Asks user for valid mark
            else:
                break #Breaks loop if mark is valid 

    if mark >= 0 and mark <= 100: #If mark is valid        
        total_mark += mark #Adds total marks

        if mark > highest_mark: #Finds highest mark 
            highest_mark = mark
    
        if mark < lowest_mark: #Finds lowest mark 
            lowest_mark = mark
    

average_mark = int((total_mark/submissions))


print("The lowest mark is", str(lowest_mark))
print("The highest mark is", str(highest_mark))
print("Your average mark is", str(average_mark))