#check if the given year is a leap year or not. leap year rules to follow:
#on every year that is divisible by 4 with no remainder
#except every year that is evenly divisible by 100 with no remainder
#unless the year is also divisible by 400 with no remainder

# Which year do you want to check?
year = int(input("Enter any year: "))

year_by4 = year % 4
year_by100 = year % 100
year_by400 = year % 400
if (year_by4==0 and year_by100 != 0):
    print ("Leap year")
elif (year_by4==0 and year_by100==0 and year_by400==0):
    print ("Leap year")  
else:
  print("Not leap year")
