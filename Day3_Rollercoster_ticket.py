#Check for age, height and give the correct fare for the ticket. $5, $7, $12.

print ("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?"))

if height >= 120:
    print ("You can ride the rollercoaster!")
    age = int(input("What's your age? "))
    bill = 0
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print ("Youth tickets are $7.")
    elif age >= 45 and age<=55:
        print("Everything is going to be ok! Have a free ride on us!!")
        # this is for people having midlife crisis - age 45 to 55.
    else:
        bill = 12
        print("Adult tickets are $12.")

    photo = input("Do you want a photo taken? Y or N. ")

    if photo == "Y" or photo == "y":
        bill += 3
        print(f"Your bill is ${bill}")
    elif photo == "N" or photo == "n":
        print(f"Your bill is ${bill}")
    else:
        print("Please re-enter either the letter 'y' or 'n'")
else:
    print("Sorry, you have to grow taller before you can ride.")
