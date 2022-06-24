user_word = input("Enter a lowercase word :")  # Prompt the user to enter a word
user_word = user_word.upper()

for letter in user_word:
    if letter == "I" or letter == "A" or letter == "E" or letter == "O" or letter == "U":
        continue
    else:
        print(letter)# Complete the body of the for loop.
