#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60



print("Welcome to the tip calculator!")
bill = eval(input("Enter the amount on the bill: "))
people = eval(input("Enter the number of people splitting it: "))
tip = eval(input("How much would you tip? 5,12,18,22? "))
tip_amount = bill + (bill*tip/100)
pay = tip_amount / people
print (f"Each person should pay {round(pay,2)}")

            
