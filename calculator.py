"""Simple Python Calculator for demonstrating Git merge conflicts."""


def add(a, b):
    """Return the sum of two numbers."""
    return a + b


def subtract(a, b):
    """Return the difference of two numbers."""
    return a - b


def calculate(num1, num2, choice):
    """Perform the selected calculation and return a formatted result."""
    if choice == "1":
        return f"Addition Result: {add(num1, num2)}"
    elif choice == "2":
        return f"Subtraction Result: {subtract(num1, num2)}"
    elif choice == "3":
        return f"Addition: {add(num1, num2)} | Subtraction: {subtract(num1, num2)}"
    else:
        return "Invalid choice! Please select 1, 2, or 3."


def main():
    print("=== Simple Python Calculator ===")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Both (Addition & Subtraction)")

    choice = input("Enter your choice (1/2/3): ").strip()

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input! Please enter valid numbers.")
        return

    print(calculate(num1, num2, choice))


if __name__ == "__main__":
    main()
