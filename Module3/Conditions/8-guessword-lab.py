secret_word = "chupacabra"
guessword = input("Guess the secret word :")
while True:
    if guessword != secret_word:
        guessword = input("Guess the secret word :")
    else:
        break
print("You've successfully left the loop.")
