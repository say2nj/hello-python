# FizzBuzz game- Fizz for divisible by 3, Buzz for divisible by 5, FizzBuzz for divisible by 3 and 5 both

for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)