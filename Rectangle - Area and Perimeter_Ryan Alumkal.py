# Name - Ryan Alumkal
# Grade - 11
# Description - Rectangle - Area and Perimieter calculator
# Date - Tuesday Febuary 8th

print("-" *65,"\n\tArea and Perimeter Calculator of a Rectangle")
print("-" *65,)

rectHeight = int(input("\nWhat is the height of the rectangle in meters: ")) #Asks the user for the height of the rectangle
rectWidth = int(input("What is the width of the rectangle in meters: ")) #Asks the user for the width of the rectangle

rectArea = rectHeight * rectWidth #Calculates area of the rectangle

rectPerimeter = (2*rectHeight) + (2*rectWidth) #Calculates perimeter of the rectangle 

print("\nThe area of the rectangle is",str(rectArea) , "meters.") #Prints area of the rectangle 

print("\nThe perimeter of the rectangle is", str(rectPerimeter), "meters.") #Prints perimeter of the rectangle 


#End of the program
