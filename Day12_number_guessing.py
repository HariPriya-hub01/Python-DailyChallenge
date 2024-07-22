#Number guessing game

#easy level - 10 guesses
#hard level - 5 guesses


#randomly generated number, you need to guess the random number.
#these are your hints: too high, too low, high, low


import random

print("Welcome to the number guessing game!\nGuess the number I have in mind.")
choose = input("Choose a difficulty level. Type 'easy' or 'hard': ").lower()
if choose == 'easy':
    num = 10
elif choose == 'hard':
    num = 5
crct_ans = random.randint(1,100)


i = 0
while i < num:
    guess = int(input("Guess a number between 1 and 100: "))
    if guess > crct_ans:
        if guess - crct_ans > 10:
            print("Too high")
        else:
            print("High")

    if guess < crct_ans:
        if crct_ans - guess > 10:
            print("Too low")
        else:
            print("Low")

    if guess == crct_ans:
        i = 100
        print("You win!")   
    i+=1
print("The ans is: ",crct_ans)
