import random

player_hand = [] 
card_deck = {
    'number_cards' : [2,3,4,5,6,7,8,9,10],
    'face' : ['A','K', 'Q', 'J' ],
}
choose = ['number_cards', 'face']



def computer():
    computer_hand = []
    total = 0
    i = 0
    computer_list = []

    while True:
        card_type = random.choice(choose)
        card_number = card_deck[card_type]
        bot_face_value = random.choice(card_number)
        #print(bot_face_value)
        computer_list.append(bot_face_value)
                 
        if bot_face_value == 'A':
            add = total + 11
            if add > 21:
                bot_face_value = 1
            else:    
                bot_face_value = 11               
        elif bot_face_value in card_deck['number_cards']:
            bot_face_value = int(bot_face_value)               
        elif bot_face_value in card_deck['face']:
            bot_face_value = 10
        total += bot_face_value
        computer_hand.append(bot_face_value)
        if total > 17:
            break 
        
    print("The computer first hand is:",computer_list[0])            
    return computer_hand
  

def player():
              
    card_type = random.choice(choose)
    #print(card_type)
    card_number = card_deck[card_type]
    p_face_value = random.choice(card_number)
    #print(f"Your card is: {p_face_value}")

    if p_face_value == 'A':
        input_for_ace = int(input(f"Ace card can be 1 or 11, what value do you want to choose for A? "))
        p_face_value = input_for_ace
                        
    elif p_face_value in card_deck['number_cards']:
        p_face_value = int(p_face_value)
            
    if p_face_value in card_deck['face']:
         p_face_value = 10
         #print("The value of this card is 10")
    return p_face_value
            


computer_hand = []
player_hand = []
player_end = False
user_total = 0

print("Welcome to Blackjack!")
start = input("Type 'y' to start playing with me or 'n' to quit: ")



while start == 'y' or start == 'Y':

    for i in range(0,2): 
        player_hand_add = player() 
        player_hand.append(player_hand_add)

    print(f"Your cards are: {player_hand}")
    user_total = sum(player_hand)
    print (f"Your total is {user_total}")

    computer_hand = computer()
    bot_total = sum(computer_hand)
    #print (f"Your total is {user_total}")
    

    while player_end == False:
       
        contd = input("Type 'y' if you want another card or type 'n' to challenge: ")
        
        if contd == 'y':
             player_hand_add = player() 
             player_hand.append(player_hand_add)
             print(f"Your cards are: {player_hand}")
             user_total = sum(player_hand)
             print (f"Your total is {user_total}")

        if user_total > 21 or bot_total > 21:
                 if user_total > 21:
                     print("You lose, your value exceeded 21!")
                     print(f"Your final hand is {player_hand} and your total {user_total}")
                     print(f"Computer final hand is {computer_hand} and its total {bot_total}")
                     player_end == True
                     break

                 if bot_total > 21:
                     print("You win!, computer value exceeded 21!")
                     print(f"Your final hand is {player_hand} and your total {user_total}")
                     print(f"Computer final hand is {computer_hand} and its total {bot_total}")
                     player_end == True
                     break

        if contd == 'n':
             if user_total > 21:
                 print("You lose, your value exceeded 21!")
                 print(f"Your final hand is {player_hand} and your total {user_total}")
                 print(f"Computer final hand is {computer_hand} and its total {bot_total}")
                 player_end == True
                 break

             if bot_total > 21:
                 print("You win!, computer value exceeded 21!")
                 print(f"Your final hand is {player_hand} and your total {user_total}")
                 print(f"Computer final hand is {computer_hand} and its total {bot_total}")
                 player_end == True
                 break
             if user_total == bot_total:
                 print("The match is a draw!")
                 print(f"Your final hand is {player_hand} and your total {user_total}")
                 print(f"Computer final hand is {computer_hand} and its total {bot_total}")
                 player_end == True
                 break
             elif user_total > bot_total:
                 print("You Win!")
                 print(f"Your final hand is {player_hand} and your total {user_total}")
                 print(f"Computer final hand is {computer_hand} and its total {bot_total}")
                 player_end == True
                 break
             elif user_total < bot_total:
                 print("You lose!")
                 print(f"Your final hand is {player_hand} and your total {user_total}")
                 print(f"Computer final hand is {computer_hand} and its total {bot_total}")
                 player_end == True
                 break          
       
    break
     
