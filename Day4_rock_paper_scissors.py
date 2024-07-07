rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""


while True:
    game = [rock, paper, scissors]
    my_turn = int(input("Your turn first!\ntype 0 for rock \ntype 1 for paper \ntype 2 for scissors\ntype 3 to quit: "))
    if 0<= my_turn <= 2:
        print ("\nYou chose:\n",game[my_turn])
    if my_turn == 3:
        break

    import random

    bot_turn = random.randint(0,2)
    print ("\nComputer chose:\n",game[bot_turn])

    if my_turn == 0 and bot_turn == 2:
        print("\nYOU WIN!!!")

    elif my_turn == 1 and bot_turn == 0:
        print("\nYOU WIN!!!")

    elif my_turn == 2 and bot_turn == 1:
        print("\nYOU WIN!!!")
     
    elif my_turn == bot_turn:
        print("\nIt's a draw!")

    elif not 0<= my_turn <= 2:
        print ("You typed an invalid number....you lose!")

    else:
        print("You lost...try again!")

    




