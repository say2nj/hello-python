fruits = ["apples","bananas","cherries"]
for fruit in fruits:
    print(fruit)
    # print(fruit,end=', ')

word = "Hello World"
for letter in word:
    print(letter, end=', ')

[print(letter) for letter in word]