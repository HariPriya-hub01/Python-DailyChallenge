'''This is a difficult challenge. 💪

You are going to write a program that will mark a spot on a map with an X.

In the starting code, you will find a variable called map.

This map contains a nested list. When map is printed this is what it looks like, notice the nesting:

[['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']]

This is a bit hard to work with. So on lines 6 and 23, we've used this line of code print(f"{line1}\n{line2}\n{line3}") to format the 3 lists to be printed as a 3 by 3 grid, each on a new line.

['⬜️', '⬜️', '⬜️']

['⬜️', '⬜️', '⬜️']

['⬜️', '⬜️', '⬜️']

Your job is to write a program that allows you to mark a square on the map using a letter-number system.


So an input of A3 should place an X at the position of the map'''

line1 = ["⬜️","⬜️","⬜️"]
line2 = ["⬜️","⬜️","⬜️"]
line3 = ["⬜️","⬜️","⬜️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
print("Look below for a reference map:")
print("   A  B  C\n 1⬜ ⬜ ⬜\n 2⬜ ⬜ ⬜\n 3⬜ ⬜ ⬜")        
position = input("Enter where you want to hide the treasure (eg: A3): ") 

item = position[0]
line_num = int(position[1])
if item == "A":
   item = 0
if item == "B":
   item = 1
if item == "C":
   item = 2
map[line_num-1][item] = "X"



print(f"{line1}\n{line2}\n{line3}")
