from art import logo


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculate(num1, num2, operation_symbol):
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    return answer


def calculator():
    print(logo)

    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    operation_symbol = input("Pick an operation from the line above: ")
    num2 = float(input("What's the second number?: "))
    answer = calculate(num1, num2, operation_symbol)

    while input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
        operation_symbol = input("Pick an operation: ")
        num = float(input("What's the next number?: "))
        answer = calculate(answer, num, operation_symbol)
    calculator()


calculator()
