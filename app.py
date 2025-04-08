def calculator():
    """
    A simple calculator function that allows users to perform basic arithmetic operations.

    The calculator provides the following operations:
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division
    5. Percentage calculation
    6. Exit the calculator

    The user is prompted to select an operation and input the required numbers. The result of the operation
    is displayed, and the user can continue performing calculations until they choose to exit.

    Features:
    - Handles invalid inputs gracefully by displaying appropriate error messages.
    - Prevents division by zero by checking the divisor before performing division.
    - Allows percentage calculation by dividing the input number by 100.

    Usage:
    Call the `calculator()` function to start the interactive calculator.
    """
    while True:
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Percentage")
        print("6. Exit")

        try:
            choice = int(input("Enter choice (1/2/3/4/5/6): "))

            if choice in [1, 2, 3, 4, 5]:
                num1 = float(input("Enter first number: "))
                if choice == 5:
                    print(f"The result is: {num1 / 100}")
                else:
                    num2 = float(input("Enter second number: "))

                    if choice == 1:
                        print(f"The result is: {num1 + num2}")
                    elif choice == 2:
                        print(f"The result is: {num1 - num2}")
                    elif choice == 3:
                        print(f"The result is: {num1 * num2}")
                    elif choice == 4:
                        if num2 != 0:
                            print(f"The result is: {num1 / num2}")
                        else:
                            print("Error: Division by zero is not allowed.")
            elif choice == 6:
                print("Exiting the calculator. Goodbye!")
                break
            else:
                print("Invalid input. Please select a valid operation.")
        except ValueError:
            print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    calculator()