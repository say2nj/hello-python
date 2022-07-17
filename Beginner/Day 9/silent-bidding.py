from art import logo
print(logo)

print("Welcome to the secret auction program.")
status = True

bid_list = []

while status:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    bid_list.append({"name": name, "bid": bid})
    continue_status = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if continue_status != 'yes':
        status = False
    print()

max_bid = 0
bidder_name = None
for bid in bid_list:
    if bid["bid"] > max_bid:
        bidder_name = bid["name"]
        max_bid = bid["bid"]

if bidder_name is not None:
    print(f"The winner is {bidder_name} with a bid of ${max_bid}.")