# Heads or Tails exercise
import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

print("Heads") if random.randint(0,1) == 1 else print("Tails")