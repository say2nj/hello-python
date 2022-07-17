# Functions

# -------Built-in Functions ---------
print("Hello")
num_char = len("Hello")
print(num_char)

# ------- User-defined functions ------
def myFunction():
    print("Hello")
    print("Bye")

myFunction()

# ------ With Argument -------
def myFunction(fname, lname):
    print("Function with argument :",fname,lname)

myFunction("Jane","Doe")

# ------ Arbitrary Arguments -----
def myFunction(*details):
    print("Function with arbitrary argument :",details[0],details[3])

myFunction("Jane","Doe","F","Developer") #Passed as a tuple

# ------ Keyword Arguments -----
def myFunction(mail, name, role):
    print("Function with keyword argument :",name,mail)

myFunction(mail="john@doe.com", role="Developer", name="John")

# ------ Arbitrary Keyword Arguments -----
def myFunction(**details):
    print("Function with arbitrary keyword argument :",details["name"],details["role"])

myFunction(mail="john@doe.com", role="Developer", name="John") # Passed as a dictionary

# Place holder for editing code later
def myFunction():
    pass

myFunction()

# return type function
def isEven(number):
    if number % 2 == 0:
        return True
    else:
        return False

print(f"5 is even number? {isEven(5)}")

#List argument to function
def myListParser(fruits):
    for fruit in fruits:
        print(fruit,end=", ")
    print("\b\b",end="")

fruits=["apples","berries","cherries"]

myListParser(fruits)