alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

from art import logo
print(logo)

finish = True
print("Welcome to Caesar Cipher!\nwe help with encoding and decoding your messages.")

while finish:
   
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    def ceasar_cipher(message, shift_by, ceasar_direction):
        final_text = ""
        if shift_by > 25:
            shift_by %= 25
            print(shift_by)
        
        if ceasar_direction == "decode":
            shift_by *= -1

        for letter in message:
            if letter in alphabet:
                position = alphabet.index(letter)
                new_position = position + shift_by
                final_letter = alphabet[new_position]
                final_text += final_letter
            else:
                final_text += letter
        print(f"The {ceasar_direction}d message is: {final_text}")
    

    ceasar_cipher(message = text, shift_by = shift, ceasar_direction = direction)
    choice = input("Types 'yes' if you want to continue. Otherwise type 'no'").lower()

    if choice == 'no':
        finish = False
        print("Alright, Goodbye!")
    

