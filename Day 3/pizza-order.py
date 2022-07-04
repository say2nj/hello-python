# Pizza Order - Exercise
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill_amount = 0

if size == 'S':
    bill_amount += 15
    if add_pepperoni == 'Y':
        bill_amount += 2
elif size == 'M':
    bill_amount += 20
    if add_pepperoni == 'Y':
        bill_amount += 3
elif size == 'L':
    bill_amount += 25
    if add_pepperoni == 'Y':
        bill_amount += 3

if extra_cheese == 'Y':
    bill_amount += 1

print(f"Your final bill is: ${bill_amount}.")