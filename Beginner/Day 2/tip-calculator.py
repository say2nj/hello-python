# Tip Calculator
print("Welcome to the tip calclator.")
bill = float(input("What was the total bill? $15"))
tip_percent = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
no_of_person = int(input("How many people to split the bill? "))
total_bill = bill + (tip_percent/100*bill)
person_share = total_bill / no_of_person
print(f"Each person should pay: ${round(person_share,2)}")