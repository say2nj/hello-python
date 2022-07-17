# Simple Function
# def greet():
#     print("Hello")
#     print("How do you do?")
#     print("Isn't the weather nice today?")
#
# greet()

# Function that allows for input

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")

greet_with_name("Nikhil")

# Function with more than 1 input

def greet_with(location, name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")
    print(f"What is it like in {location}?")

greet_with( name = "Nikhil", location = "Delhi")