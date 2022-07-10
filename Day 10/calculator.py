from art import logo


def add(num1, num2):
    return num1 + num2


def minus(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


operations = {"+": add, "-": minus, "*": multiply, "/": divide}


def calculator():
    print(logo)
    status = True
    number1 = float(input("What's the first number?: "))
    while status:
        for ops in operations.keys():
            print(ops)
        operation_choice = input("Pick an operation: ")
        if operation_choice in operations.keys():
            number2 = float(input("What's the next number?: "))
            result = operations[operation_choice](number1, number2)
            print(f"{number1} {operation_choice} {number2} = {result}")
            user_choice = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
            if user_choice == 'y':
                number1 = result
            elif user_choice == 'n':
                calculator()
            else:
                status = False
        else:
            status = False


calculator()
