#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# open invited names
with open("Input/Names/invited_names.txt", "r") as invited_names:
    first_invited = str(invited_names.readlines(1)).strip()
    print(first_invited)


# Open the starting letter
with open("Input/Letters/starting_letter.txt", "r") as letter:
    first_line = str(letter.readlines(1))
    changed_name = first_line.replace("name", first_invited)
    print(first_line)





