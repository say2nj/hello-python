# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

age = int(age)

remaining_years = 90-age
print(f"Remaining Years: {remaining_years}")

remaining_months = remaining_years * 12
remaining_weeks = remaining_years * 52
remaining_days = remaining_years * 365
print(f"You have {remaining_days} days, {remaining_weeks} weeks, and {remaining_months} months left.")

