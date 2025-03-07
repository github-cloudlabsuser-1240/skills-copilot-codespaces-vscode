def add(x, y):
    """
    Adds two numbers together.

    Args:
        x (int or float): The first number.
        y (int or float): The second number.

    Returns:
        int or float: The sum of x and y.
    """
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def percentage(x, y):
    if y == 0:
        raise ValueError("Error: Division by zero")
    return (x / y) * 100

def main():
    """
    Main function to perform basic arithmetic operations.

    Prompts the user to select an operation from the following:
    1. Add
    2. Subtract
    3. Multiply
    4. Percentage

    Then, it takes two numerical inputs from the user and performs the selected operation.

    Raises:
        ValueError: If the input is invalid or if an error occurs during the operation.
    """
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Percentage")

    choice = input("Enter choice(1/2/3/4): ")

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if choice == '1':
            print(f"The result is: {add(num1, num2)}")
        elif choice == '2':
            print(f"The result is: {subtract(num1, num2)}")
        elif choice == '3':
            print(f"The result is: {multiply(num1, num2)}")
        elif choice == '4':
            print(f"The result is: {percentage(num1, num2)}%")
        else:
            print("Invalid input")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()