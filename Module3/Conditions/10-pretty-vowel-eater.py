word_without_vowels = ""

user_word = input("Enter a word :")  # Prompt the user to enter a word
user_word = user_word.upper()

for letter in user_word:
    if letter == "I" or letter == "A" or letter == "E" or letter == "O" or letter == "U":
        continue
    else:
        word_without_vowels += letter  # Complete the body of the loop.
print(word_without_vowels)  # Print the word assigned to word_without_vowels.
