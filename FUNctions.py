"""
Name: Ryan Alumkal
Date: Wednesday, 18, 2022
File Name: FUNctions.py
Description: Calcualtes slope of 2 points on a graph, also calculates sum of first integers specified by user and sum of the first integers specified by the user
"""
#functions 
def print_header(): #prints header
    print("Name: Ryan Alumkal")
    print("Date: Wednesday, 18, 2022")
    print("File Name: FUNctions.py")
    print("Description: Calcualtes slope of 2 points on a graph, also calculates sum of first integers specified by user and sum of the first integers specified by the user")

def slope(x1, y1, x2, y2): #slope calcuation function
    try:
        slope = round((y2-y1)/(x2-x1),2) #calculates slope 
        if slope == -0.0: #if slope is -0.0, happens when slope is meant to be 0
            slope = 0#corrects slope 
        return slope
    except: #if slope is undefined 
        return "undefined" #returns the string "undefined"

def fancy_sum(n):
    #variables 
    num_sum = 0 
    sum_of_squares = 0
    for i in range(1,n+1): #numbers till number specified
        num_sum +=i #sum of numbers till n
        sum_of_squares += i**2 #sum of squares till n
    return num_sum,sum_of_squares #returns sums 
  
#Main program
main_loop = True
n = 0
while main_loop: #main loop for main menu
  loop = True 
  user_function = 4
  print("---MAIN MENU---")
  while user_function != 1 and user_function != 2 and user_function !=3: 
    try:
      user_function = int(input("ENTER 1 TO SEE HEADER \nENTER 2 TO FIND SLOPE \nENTER 3 TO FIND VARIOUS SUMS OF NUMBER \nENTER NUMBER: ")) #asks user for function to run
    except: #if invalid data type 
      print("Enter a valid input (1,2,or 3)") #if input is an invalid data type
    if user_function <= 0 or user_function >=4: #if invalid input
      print("Enter a valid input (1,2,or 3)") #if input is invalid 
      
  if user_function == 1: #if user wants to run header 
    print_header() #header 
  elif user_function == 2: #if user wants to find slope 
       while loop: #while loop is true 
        try:
            #user inputs for points 
            x1 = int(input("Enter the x value of your first point: "))
            y1 = int(input("Enter the y value of your first point: "))
            x2 = int(input("Enter the x value of your second point: "))
            y2 = int(input("Enter the y value of your second point: "))
            slope_of_line = slope(x1,y1,x2,y2) #slope calculation 
            print(f"The slope of the line is {slope_of_line}") #results
            loop = False #breaks loop
        except:
            print("One of the values are invalid") #if input is invalid
       
  elif user_function == 3: #if user wants to find various sums of a number
      while n <= 0: #while n is invalid
        try:
            n = int(input("What is the number you want to calculate: ")) #number to calculate
            values = fancy_sum(n) #fancy sum
            print(f"The sum of the first {n} integers is {values[0]}, the sum of the squares of the first {n} integers is {values[1]}") #results of fancy sum
        except:
            print("Invalid input") #if input is invalid

  user_continue = int(input("Enter 1 to continue or 2 to end the program: ")) #if user wants to continue or en
  if user_continue == 1: #if 1, continue 
    continue
  elif user_continue == 2: #if 2, end 
    print("Thank you for using the program")
    loop = False
    main_loop = False