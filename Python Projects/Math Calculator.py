import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."

def square_root(a):
    try:
        if a < 0:
            raise ValueError("Cannot calculate the square root of a negative number.")
        return math.sqrt(a)
    except ValueError as e:
        return str(e)

def exponentiate(a, b):
    return a ** b

def calculator():
    print("Welcome to the Basic Calculator!")
    print("Available operations:")
    print("1. Addition (a + b)")
    print("2. Subtraction (a - b)")
    print("3. Multiplication (a * b)")
    print("4. Division (a / b)")
    print("5. Square Root (sqrt(a))")
    print("6. Exponentiation (a ^ b)")
    print("Type 'quit' to exit the calculator.")

    while True:
        operation = input("\nChoose an operation (1-6) or 'quit': ").strip().lower()

        if operation == 'quit':
            print("Thanks for using the calculator. Goodbye!")
            break

        if operation not in {'1', '2', '3', '4', '5', '6'}:
            print("Invalid choice. Please choose a valid operation.")
            continue

        if operation == '5':  # Square root
            try:
                num = float(input("Enter the number: "))
                result = square_root(num)
                print(f"Result: {result}")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        else:
            try:
                num1 = float(input("Enter the first number: "))
                num2 = None
                if operation != '5':
                    num2 = float(input("Enter the second number: "))

                if operation == '1':
                    result = add(num1, num2)
                elif operation == '2':
                    result = subtract(num1, num2)
                elif operation == '3':
                    result = multiply(num1, num2)
                elif operation == '4':
                    result = divide(num1, num2)
                elif operation == '6':
                    result = exponentiate(num1, num2)

                print(f"Result: {result}")
            except ValueError:
                print("Invalid input. Please enter valid numbers.")

if __name__ == "__main__":
    calculator()
