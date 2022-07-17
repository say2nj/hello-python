from art import logo
from random import choice
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def draw_cards():
    return choice(cards)

def calculate_score(cards):
    if len(cards) == 2 and 11 in cards and 10 in cards:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, comp_score):
    if user_score == comp_score:
        return "Draw 😪"
    elif comp_score == 0:
        return "Lose, opponent has Blackjack 👀"
    elif user_score == 0:
        return "You win with a Blackjack"
    elif user_score > 21:
        return "You went over. You lose 🤢"
    elif comp_score > 21:
        return "Opponent went over. You win 😃"
    elif user_score > comp_score:
        return "You Win!"
    else:
        return "You Lose"

def blackjack_game():
    print(logo)

    user_cards = []
    comp_cards = []

    for _ in range(2):
        user_cards.append(draw_cards())
        comp_cards.append(draw_cards())

    print(f"    Your cards: {user_cards}")
    print(f"    Computer's first card: {comp_cards[0]}")

    game_status = True

    while game_status:
        user_cards_sum = calculate_score(user_cards)
        comp_cards_sum = calculate_score(comp_cards)


        if user_cards_sum == 0 or comp_cards_sum == 0 or user_cards_sum > 21:
            game_status = False
        else:
            user_input = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_input == 'y':
                user_cards.append(draw_cards())
            else:
                game_status = False

    while comp_cards_sum != 0 and comp_cards_sum < 17:
        comp_cards.append(draw_cards())
        comp_cards_sum = sum(comp_cards)

    print(f"    Your cards: {user_cards} , Your score: {user_cards_sum}")
    print(f"    Computer's first card: {comp_cards}, Computer score: {comp_cards_sum}")
    print(compare(user_cards_sum, comp_cards_sum))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == 'y':
    blackjack_game()
