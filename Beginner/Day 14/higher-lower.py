from art import logo, vs
from data import data
from random import choice

print(logo)

option1 = choice(data)
status = True

def assign_option2():
    option2 = choice(data)
    if option2 == option1:
        option2 = assign_option2()
    return option2

score = 0
while status:
    option2 = assign_option2()
    print(f"Compare A: {option1['name']}, {option1['description']}, from {option1['country']}.")
    print(vs)
    print(f"Against B: {option2['name']}, {option2['description']}, from {option2['country']}.")
    # print(option1['follower_count'] , option2['follower_count'])
    winner = 'A' if option1['follower_count'] > option2['follower_count'] else 'B'
    user_input = input("Who has more followers? Type 'A' or 'B': ").lower()
    if user_input == winner:
        score += 1
        print(f"You're right! Current score: {score}.")
        option1 = option2
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        status = False
