import math

def paint_calc(height, width, cover):
    area = test_h * test_w
    num_of_cans = math.ceil(area / coverage)
    print(f"You'll need {num_of_cans} cans of paint.")

# Define a function called paint_calc() so that the code below works.

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

