#Create a program using maths and f-Strings that tells us,
#how many weeks we have left, if we live until 90 years old.

age = input("Enter your age: ")
time_left = (90 - int(age))*52
print( f"You have {time_left} weeks left." )
