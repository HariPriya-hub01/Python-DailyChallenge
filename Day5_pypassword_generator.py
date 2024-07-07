# Pypassword generator project! generate a random password.

letter = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
letter_caps = []
for i in letter:
    letter_caps.append(i.upper())
letter+=letter_caps
#print(letter)

number = ['0','1','2','3','4','5','6','7','8','9']
char = ['!','@','#','$','%','^','&','*','(',')','_','-','+']

letter_no = int(input("How many letters you want in your password:  "))
char_no = int(input("How many characters do you like? "))
number_no = int(input("How many numbers would you want? "))

letter_list = []
letter_caps_list = []
number_list = []
char_list = []
final = []
final_list = []

import random


for i in range(0,letter_no):
    rand = random.randint(0,len(letter)-1)    
    letter_rand = letter[rand]
    letter_list.append(letter_rand)
    

for j in range(0,number_no):
    rand = random.randint(0,9)
    number_rand = number[rand]
    number_list.append(number_rand)


for k in range(char_no):
    rand = random.randint(0,12)
    char_rand = char[rand]
    char_list.append(char_rand)


total = letter_no+char_no+number_no
final = letter_list+number_list+char_list
#final =''.join(letter_list+number_list+char_list) -> this definitely works in converting list to string!

random.shuffle(final)
final_password = ""
for i in final:
    final_password+=i
    
print(f"Your password is: {final_password}")






#print("Your password is: ",str(final)) -> this type of conversion does nothing, its still a list

'''for l in range(0,total-1):
    rand = random.randint(0,total)
    final_rand = final[rand]
    final_list.append(final_rand)''' #the random characters became random again and got repeated. not ideal!


    
#####################################################################################################################    

#Eazy Level
# password = ""

# for char in range(1, nr_letters + 1):
#   password += random.choice(letters)

# for char in range(1, nr_symbols + 1):
#   password += random.choice(symbols)

# for char in range(1, nr_numbers + 1):
#   password += random.choice(numbers)

# print(password)

######################################################################################################################

#Hard Level
'''password_list = []

for char in range(1, nr_letters + 1):
  password_list.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
  password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
  password_list += random.choice(numbers)

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
  password += char

print(f"Your password is: {password}")'''
