"""A minimal four‑function calculator used for Git practice."""

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

if __name__ == "__main__":
    x = float(input("First number: "))
    y = float(input("Second number: "))
    op = input("Choose [+ - * /]: ").strip()

    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
    }

    try:
        result = operations[op](x, y)
        print("Result:", result)
    except KeyError:
        print("Unsupported operator")