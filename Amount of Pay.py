# Name - Ryan Alumkal
# Grade - 11
# Description - Calculates the amount of pay for a user per week: part-time, full-time, and overtime
# Date - Tuesday Febuary 20th

print("-" *30,"\n\tPay Calculator") 
print("-" *30,)
#Graphic

user_hours = float(input("How many hours did you work this week (please enter a number, can be whole number or decimal  numbers): "))
#Asks user for the amount of hours they worked in a week

while user_hours < 0:
  user_hours = float(input("Please input a valid number (greater than 0): "))
#While hours are less than 0, keep asking for a valid value

if user_hours >= 20: #If user is a full time employee
  user_position = "Full-Time Employee" #Position
  user_wage = 15.00 #Hourly wage 
  if user_hours > 40: #If user has worked more than 40 hours, overtime
    user_pay = 40 * user_wage #Calculates pay before overtime
    user_overtime_wage = 22.50 #Overtime pay 
    user_pay = user_pay + (( user_hours - 40)* user_overtime_wage) #Calculates pay including overtime pay
    print("\nYou are a", str(user_position)) #Prints user position 
    print("Your total pay for", user_hours, "hours at $"+ str(user_wage) + "/hr at normal rate and $"+ str(user_overtime_wage) + "/hr at overtime rate was $" + str(user_pay)) #Provides information: hours, wage, overtime wage, and total pay
  else: #If user has worked less than or equal to 40
    user_pay = user_hours * user_wage #Calculates pay for full time employees without overtime 
    print("\nYou are a", str(user_position)) #Prints user position 
    print("Your total pay for",user_hours, "hours at $"+ str(user_wage) +"/hr at normal rate was $" + str(user_pay)) #Provides information: hours, wage, and pay
elif user_hours > 0: #If user is a part-time worker 
  user_position = "Part-Time Employee" #Position 
  user_wage = 10.00 #Hourly wage 
  user_pay = user_hours * user_wage #Calculates pay for part time 
  print("\nYou are a", str(user_position)) #Prints user position 
  print("Your total pay for",user_hours, "hours at $"+ str(user_wage) +"/hr at normal rate was $" + str(user_pay)) #Provides information: hours, wage, and pay
elif user_hours == 0: #If user hasn't worked this week
  print("You haven't worked this week!")

#END OF PROGRAM 
