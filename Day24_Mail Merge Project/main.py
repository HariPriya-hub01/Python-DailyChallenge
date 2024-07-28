#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp



with open("./Input/Names/invited_names.txt") as names_list:
    guest_name = names_list.readlines()
    #print(guest_name)

with open("./Input/Letters/starting_letter.txt") as main_letter:
    main_letter_content = main_letter.read()
    #print(main_letter_content)
    for name in guest_name:
        name = name.strip("\n")
        new_letter = main_letter_content.replace("[name]", name)
        #print(new_letter)
        with open(f"./Output/ReadyToSend/letter_to_{name}.txt", mode="w") as end_letter:
            end_letter.write(new_letter)
