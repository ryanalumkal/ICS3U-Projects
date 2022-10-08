# Name - Ryan Alumkal
# Grade - 11
# Description - Orders 3 integers from least to greatest
# Date - Wednesday Febuary 23th

#User Inputs 
user_num1 = int(input("Input a number (integer value): "))
user_num2 = int(input("Input a number (integer value): "))
user_num3 = int(input("Input a number (integer value): "))

#Conditions

if user_num1 == user_num2:  #If 2 numbers are equal 
    largest = user_num1
    middle = user_num2
    if middle > user_num3: #If numbers 1 and 2 are greater than number 3
        lowest = user_num3 
    elif middle <= user_num3: #If numbers 1 and 2 are lesser than or equal to number 3
        largest = user_num3 
        middle = user_num2
        lowest = user_num1
      
elif user_num1 == user_num3:  #If numbers 1 and 3 are equal 
    largest = user_num1
    middle = user_num3
    if middle > user_num2: #If numbers 1 and 3 are greater than number 2
        lowest = user_num2
    elif middle < user_num2: #If numbers 1 and 3 are less than number 2 
        largest = user_num2 
        middle = user_num3
        lowest = user_num1
      
elif user_num2 == user_num3: #If numbers 2 and 3 are equal 
  largest = user_num2
  middle = user_num3
  if middle > user_num1: #If numbers 2 and 3 are greater than number 1 
    lowest = user_num1
  elif middle < user_num1: #If numbers 2 and 3 are less than number 1 
    largest = user_num1
    middle = user_num2
    lowest = user_num3  
    
elif user_num1 > user_num2: #If number 1 is greater than number 2 
    largest = user_num1
    middle = user_num2
    if middle > user_num3: #If number 2 is greater than number 3
        lowest = user_num3
    elif largest < user_num3: #If number 3 is larger than number 1
      largest = user_num3
      middle = user_num1
      lowest = user_num2
    elif middle < user_num3: #If number 3 is larger than the middle number
        middle = user_num3
        lowest = user_num2   
      
elif user_num1 < user_num2: #If number 1 is less than number 2 
    largest = user_num2
    middle = user_num1
    if middle > user_num3: #If number 1 is greater than number 3  
        lowest = user_num3
    elif largest < user_num3: #If number 2 is less than number 3 
      largest = user_num3
      middle = user_num2
      lowest = user_num1
    elif middle < user_num3: #If number 3 is greater than number 1 
        middle = user_num3
        lowest = user_num1

    
print("The order from least to greatest is ", str(lowest), str(middle), str(largest))  #PRINTS RESULTS
