# Name - Ryan Alumkal
# Grade - 11
# Description - Asks user for radius, then calculates area and circumference. Continues if user wants to
# Date - Friday May 6th, 2022
import math 
radius = -1
loop = True

def circumferece(r):
  circumferece_circle = round(2*math.pi*r,2)
  return circumferece_circle

def area(r):
  area_circle = round(math.pi*(r**2),2)
  return area_circle 
  
def get_radius(radius):
  while radius <= 0:
    try:  
      radius = float(input("What is the radius of the circle (Greater than 0): "))
    except:
      print("Enter a valid value (float and greater than 0)")
    if radius <=0:
      print("Enter a valid greater than 0")
    else:
       return radius

#main program 
while loop: #While user wants to rurn program again 
  user_loop = True 
  r = get_radius(radius) #gets radius from user 
  circumferece_circle = circumferece(r) #holds circumference of the circle 
  area_circle =  area(r) #holds area of the circle 
  print(f"The circumference of the circle is {circumferece_circle}") #prints circumference 
  print(f"The area of the circle is {area_circle}") #prints area 
  while user_loop: #asks user if they want to run program again
    user_continue = input("Do you want to continue? (Y for yes, N for no):") #Asks user for an answer 
   
    if user_continue.lower() == "y" or user_continue.lower() == "yes":#if user wants to continue
      pass #goes back to the main loop
      user_loop = False #breaks loop
    elif user_continue.lower() == "n" or user_continue.lower() =="no": #if user wants to stop
      print("Thanks for using the program! See you later.")
      loop = False #breaks main loop 
      user_loop = False #breaks loop
    else: #if input is not valid
      print("Enter a valid input")