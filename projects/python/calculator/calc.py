import math

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def power(num1, num2):
    return num1 ** num2

def square_root(num):
    return math.sqrt(num)

def percentage(num, perc):
    return (perc / 100) * num


number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /, ^, sqrt, %): ")

match operation:
    case "+":
        result = add(number1, number2)
        print("The result of the addition is:", result)
    case "-":
        result = subtract(number1, number2)
        print("The result of the subtraction is:", result)
    case "*":
        result = multiply(number1, number2)
        print("The result of the multiplication is:", result)
    case "/":
        if number2 == 0:
            print("Error: division by zero.")
        else:
            result = divide(number1, number2)
            print("The result of the division is:", result)
    case "^":
        result = power(number1, number2)
        print("The result of the power is:", result)
    case "sqrt":
        if number1 < 0:
            print("Error: cannot calculate the square root of a negative number.")
        else:
            result = square_root(number1)
            print("The result of the square root is:", result)
    case "%":
        result = percentage(number1, number2)
        print("The result of the percentage is:", result)
    case _:
        print("Invalid operation. Please enter a valid operation (+, -, *, /, ^, sqrt, %).")
