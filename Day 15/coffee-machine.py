from data import resources_data, MENU

resources = resources_data
money = 0
status = True


def check_resources(item):
    """Check the resource availability for making coffee"""
    for x in MENU[item]['ingredients'].keys():
        if MENU[item]['ingredients'][x] >= resources[x]:
            print(f"Sorry there is not enough {x}.")
            return False
    return True


def reduce_resources(item):
    """Deduct the resource amount based on consumption by recipe"""
    for x in MENU[item]['ingredients'].keys():
        resources[x] -= MENU[item]['ingredients'][x]


def process_coins(item):
    """To process changes exchanged and total amount earned"""
    global money
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))
    payed = (pennies * 0.01) + (dimes * 0.1) + (nickels * 0.05) + (quarters * 0.25)
    if payed < MENU[item]['cost']:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        if (payed - MENU[item]['cost']) != 0:
            print("Here is $%.2f in change." % (payed - MENU[item]['cost']))
        money += MENU[item]['cost']
        return True


while status:
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_input == 'report':
        resource = resources.keys()
        for i in resource:
            if str(i) in ('water', 'milk'):
                print(f"{str(i).capitalize()}: {str(resources[i])}ml")
            elif str(i) == 'coffee':
                print(f"{str(i).capitalize()}: {str(resources[i])}g")
        print(f"Money: ${money}")

    elif user_input in ('espresso', 'latte', 'cappuccino'):
        resource_status = check_resources(user_input)
        if resource_status:
            if process_coins(user_input):
                print(f"Here is your {user_input} ☕ Enjoy!")
                reduce_resources(user_input)

    elif user_input in ('refill', 'maintenance'):
        resources["water"] = 300
        resources["milk"] = 200
        resources["coffee"] = 100

    elif user_input == 'stop':
        status = False

    else:
        status = False
