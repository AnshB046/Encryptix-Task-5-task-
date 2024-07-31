def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"


def main():
    print("Welcome to the Simple Calculator!")

    while True:
        print("\nEnter two numbers:")
        num1 = float(input("First number: "))
        num2 = float(input("Second number: "))

        print("\nChoose an operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            result = add(num1, num2)
            print(f"Result: {num1} + {num2} = {result}")
        elif choice == "2":
            result = subtract(num1, num2)
            print(f"Result: {num1} - {num2} = {result}")
        elif choice == "3":
            result = multiply(num1, num2)
            print(f"Result: {num1} * {num2} = {result}")
        elif choice == "4":
            result = divide(num1, num2)
            print(f"Result: {num1} / {num2} = {result}")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
