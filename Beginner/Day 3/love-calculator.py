# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

combined_name = name1.lower() + name2.lower()

count_T = combined_name.count('t')
count_R = combined_name.count('r')
count_U = combined_name.count('u')
count_E = combined_name.count('e')

count_L = combined_name.count('l')
count_O = combined_name.count('o')
count_V = combined_name.count('v')

score_true = str(count_T + count_R + count_U + count_E)
score_love = str(count_L + count_O + count_V + count_E)

love_percent = int(score_true+score_love)

if love_percent < 10 or love_percent > 90:
    print(f"Your score is {love_percent}, you go together like coke and mentos.")
elif love_percent > 40 or love_percent < 50:
    print(f"Your score is {love_percent}, you are alright together.")
else:
    print(f"Your score is {love_percent}.")
