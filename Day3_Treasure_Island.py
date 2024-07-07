print ("Welcome to treasure island!")
print (''' _                                     _     _                 _
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|''')


print ("Let's see if you can find the hidden treasure!")

direction = input ("You are standing at the top of a hill, do yoy want to go left or right? ")
direction = direction.lower()
if direction == "right":
    print ("\nJust because you chose 'right' doesn't mean you are on the right direction!")
    
    print ("oops! Its a cliff!")
   
    print ("You fall from the cliff....reflect on your bad choices in life.....and game over")
   
    print ("Someone people like you die even before the game starts...") 
if direction == "left":
   print ("\ngreat! you just walked down the hill and you are now at a beach!")
  
   sail = input("you see a boat and a ship, which one would you choose?")
   sail = sail.lower()
   if sail == "boat":
       print ("\nSeriosly? a boat? to a treasure island?....well, get on the boat! let's go!")
   
       print ("Looks like you are at the same place you started an hour ago...")
     
       print (".....still rowing the boat to this day..The end!")
     
       print ("Treasure? what treasure?...LOSER!")
   if sail == "ship":
       confirm = input("\nThis ship is filled with scary pirates, do you still want to enter? y or n?")
       confirm = confirm.lower()
       if  confirm == "n":
           print ("\nWhy? afraid they would kill you?")
           
           print ("Don't even think about the boat, it's no longer there!")
          
           print ("What are you gonna do now? you are too dumb for this game!")
           
           print ("Just quit playing")
       if confirm == "y":
             print("\nyou are right! don't judge a book by its cover, they are friendly after all!")
             
             answer = input("The captain wants to know where you are going to, what are you gonna say? the truth? or lie?")
             answer = answer.lower()
             if answer == "lie":
                  print ("\nLooks like they believed you! they think you are an explorer.")
                  
                  island = input("There are 3 islands on the way, which one do you want to go? 1, 2 or 3?")

                  if island == "2":
                       print ("\nYou just landed safe! walk a little further into the woods")
                       
                       house = input("It is getting dark, there are two houses in front of you, one is a small hut and another is a tent.\nWhich one do you choose for the night? hut or tent?")
                       house = house.lower()
                       if house == "hut":
                            print("\noh! its a warm and cozy place to sleep but look there are three holes on the ground with different trapdoors")
                            
                            door = input("There is a golden door, a silver and a plastic door, which one would you choose? gold, silver or plastic?")
                            if door == "silver":
                                 print("\nopen the door! see there is an old suitcase and also an angry snake!")
                                 
                                 risk = input("What are you going to do? close the door and leave or risk your life to get the suitcase? leave or risk?")
                                 risk = risk.lower()
                                 if risk == "risk":
                                     print ("\nOh looks like its an old toothless snake, lmao! Now open the suitcase")
                                     
                                     print ('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')
                                     print ("\nYay!! you got the treasure!\nYOU WIN!")
                                     
                                 elif risk == "leave":
                                     print ("\nYou seem to be a chicken...get the heck out of here you loser!")
                            elif door == "gold":
                                 print ("\nopen the door! Oh no, its empty...I had high hopes too")
                                 
                                 print ("On the bright side, you atleast got the golden door! lets just say that's the one we are looking for.")
                                 
                                 print ("Bon voyage, lOSER!")
                            elif door == "plastic":
                                 print ("\nOpen the door! is it empty?")
                                 
                                 print ("Well, what did you expect? a treasure hidden under a plastic door? you need more brains than that!")
                                 
                                 print ("Bye, bye, loser!")
                       elif house == "tent":
                            print ("\nA huge hurricane lifts the tent up and you fly away into the clouds...*ting*")
                            
                            print ("choosing a tent to sleep in the middle of nowhere doesn't seem too bright to me!")
                            
                            print ("Please don't play again, loser!")
                  elif island == "1":
                        print ("\nThis place seems so dark even in broad daylight!")
                        
                        print ("Oh no! this is an enchanted island! Look there comes the witch!!")
                        
                        print ("The witch casts a spell and turns you into a frog!\nWell, that's how the story of 'The frog prince' began...")
                        
                        print ("No treasure for you! YOU LOSE!\n....this swamp full of insects must be your treasure, LoL!")
                  elif island == "3":
                        print ("\nUmm...well...This is a really small mysterious island and you know what they say? People who went in never got out!!")
                        
                        print ("Just jump in the water with the sharks...die...and play again.")
             elif answer == "truth":
                  print ("\nThe Captain pulls you by the neck and says, 'That's my treasure and none alive should breathe about it'")
                  
                  print ("Pulls out a sword and kills you")
                  
                  print ("Seriously?..talking about a treasure to a pirate? You should know better, LOSER!")


                         
