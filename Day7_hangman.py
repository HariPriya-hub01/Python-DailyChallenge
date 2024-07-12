#Step 1 is the first line in every TODO, step 2 starts with #, 

#print(words_list[0])


#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
          #For each letter in the chosen_word, add a "_" to 'display'.
          #So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
          #If the letter at that position matches 'guess' then reveal that letter in the display at that position.
          #e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
          #Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.

#Step 4: Use a while loop to let the user guess again.
#The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.'''


from words_list import words_list


hangman = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']



import random

print("""
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                         """)

print("Welcome to Hangman")

guess_word = random.choice(words_list).lower()

user_list = []
blank = []
lost_count = 0
for i in range(0,len(guess_word)):
    blank += '_'
print("Guess this word:\n",blank)

while lost_count < 6:
    user_input = input("Enter a letter: ").lower()
    

    if user_input in user_list:
        print("You have already guesses this letter")
        user_input = input("Enter another letter: ").lower()

    user_list.append(user_input)
    

    for i in range(len(guess_word)):
        if guess_word[i] == user_input:
            blank[i] = user_input
    if user_input not in guess_word:
        lost_count += 1
        print("You guessed wrong! you lose a life!")
        print(hangman[lost_count])

    print(blank)

    if '_' not in blank:
        print(f"yes! The word is: {guess_word}")
        print("You Win!")
        
        break

if '_' in blank:
    print("You lost, you lost all your lives.")
    print(f"The word is: {guess_word}")
        





    
