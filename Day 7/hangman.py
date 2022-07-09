from art import logo, stages
from words import word_list
from random import choice

# Displaying hangman logo
print(logo)

# Selecting a random word from a list
selected_word = choice(word_list)

# selected_word = "Bizarre".lower() -- For dev purpose

# Variables- Intiializing
length = len(selected_word)
lives = 6
secret_word= []
end_of_game = False

# Creating a list of display string
for x in selected_word:
    secret_word.append("_")

# Looping
while not end_of_game:
    letter = input("Guess a letter: ").lower()

    # If letter matches in selected word
    if letter in selected_word:
        for position in range(length):
            if selected_word[position] == letter:
                secret_word[position] = letter
        [print(x, end=" ") for x in secret_word]
        print(stages[lives])
        if '_' not in secret_word:
            print("You win.")
            end_of_game = True

    # If letter doesn't exists, then deduct a life
    elif letter not in selected_word:
        lives -= 1
        [print (x, end=" ") for x in secret_word]
        print(f"\nYou guessed {letter}, that's not in the word. You lose a life.")
        if lives == 0:
            end_of_game = True
        print(stages[lives])
        print("Game over")
