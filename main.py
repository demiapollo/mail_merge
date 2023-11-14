PLACEHOLDER = "[name]"

# open invited names
with open("Input/Names/invited_names.txt", "r") as names_file:
    names = names_file.readlines()
    print(names)


# Open the starting letter
with open("Input/Letters/starting_letter.txt", "r") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"Output/ReadytoSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)





