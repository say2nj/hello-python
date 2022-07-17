from random import randint
from art import rock, paper, scissors

new_list = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choice in [0,1,2]:
    print(new_list[user_choice])
    computer_choice = randint(0,2)
    print("Computer chose: ")
    print(new_list[computer_choice])

    if computer_choice == user_choice:
        print("It's a Draw.")
    elif user_choice == 0:
        print("You Win!") if computer_choice == 2 else print("You Lose!")
    elif user_choice == 1:
        print("You Win!") if computer_choice == 0 else print("You Lose!")
    elif user_choice == 2:
        print("You Win!") if computer_choice == 1 else print("You Lose!")

else:
    print("Invalid Choice")