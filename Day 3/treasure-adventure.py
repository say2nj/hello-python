from art import treasure

print(treasure)
print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
step1 = input("""You're at a cross road. Where do you want to go? Type "left" or "right" """).lower()
if step1 == 'left':
    step2 = input("""You come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat \
or "swim" to swim across. """).lower()
    if step2 == 'wait':
        step3 = input("""You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one\
blue. Which color do you choose? """).lower()
        if step3 == 'blue':
            print("You enter a room of beasts. Game Over.")
        elif step3 == 'red':
            print("It's a room full of fire. Game Over.")
        elif step3 == 'yellow':
            print("You found the treasure! You win!")
        else:
            print("Invalid Choice. Game over")
    elif step2 == 'swim':
        print("You got attacked by an angry trout. Game Over.")
    else:
        print("Invalid Choice. Game Over")
elif step1 == 'right':
    print("You fell into a hole. Game Over.")
else:
    print("Invalid Choice. Game over")