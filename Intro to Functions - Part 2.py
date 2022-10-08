# Name - Ryan Alumkal
# Grade - 11
# Description - Asks user for the 3 sides of a triangle to calculate area 
# Date - Friday May 6th, 2022

#Variable initialize 
a = 0 
b = 0
c = 0

import math

#functions 
def inputs(a,b,c): #asks user for input 
  while a <=0 and b <=0 and c <=0:
    try:
      a = int(input("What is one side length of the triangle (greater than 0): ")) #asks user for input
      b = int(input("What is another side length of the triangle (greater than 0): ")) #asks user for input
      c = int(input("What is the last side length of the triangle (greater than 0): ")) #asks user for input
    except:
      print("Please enter a valid integer number") #if input is not  a valid data type
    if a <=0 and b <=0 and c <=0: #if input is not valid (less than or equal to 0)
        print("One or more of your parameters are invalid! Enter a valid integer with a value greater than 0")
    else: #if input is valid 
      return a,b,c
  
def area(a,b,c): #calculates area of the triangle 
  #heron's formula 
  p = (a+b+c)/2 
  area = round(math.sqrt((p*(p-a)*(p-b)*(p-c))),1)
  print(f"The area of the triangle is about {area}") #prints out the area 
  return area

def height(area,parameters): #calculates heights 
  height1 = round((area*2)/parameters[0],1) #height with one base
  height2 = round((area*2)/parameters[1],1) #height with another base
  height3 = round((area*2)/parameters[2],1) #height with the last base

  #prints out results 
  print(f"The height of the triangle with a base of {parameters[0]} is {height1}")
  print(f"The height of the triangle with a base of {parameters[1]} is {height2}")
  print(f"The height of the triangle with a base of {parameters[2]} is {height3}")

#main program 
parameters = inputs(a,b,c) #holds parameters from user input
area = area(parameters[0], parameters[1],parameters[2]) #holds area of triangle
height(area,parameters) #used to calculate heights of the triangle 