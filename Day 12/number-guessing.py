from random import randint
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
random_number = randint(1, 100)
difficulty_level = input("Choose a difficulty.Type 'easy' or 'hard': ")
attempts = None
if difficulty_level == 'hard':
    attempts = 5
elif difficulty_level == 'easy':
    attempts = 10

print(f"You have {attempts} attempts remaining to guess the number.")

status = True


def reduce_attempt():
    global attempts
    attempts -= 1


def check_attempt():
    if attempts == 0:
        print("You've run out of guesses, you lose.")
        return False
    elif attempts > 0:
        print("Guess again.")
        print(f"You have {attempts} attempts remaining to guess the number.")
        return True


while status:

    guess_number = int(input("Make a guess: "))
    if guess_number == random_number:
        print(f"You got it! The answer was {random_number}")
        status = False
    elif guess_number < random_number:
        print("Too low.")
        reduce_attempt()
        status = check_attempt()
    elif guess_number > random_number:
        print("Too high.")
        reduce_attempt()
        status = check_attempt()
