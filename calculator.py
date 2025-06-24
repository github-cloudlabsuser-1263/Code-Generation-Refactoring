def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

if __name__ == "__main__":
    print("=== Basic Calculator ===")
    while True:
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Enter choice (1/2/3/4/5): ").strip()

        if choice == '5':
            print("Thank you for using the calculator. Goodbye!")
            break

        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("\n[Error] Invalid input. Please enter valid numbers.")
                continue

            if choice == '1':
                result = add(num1, num2)
                op = '+'
            elif choice == '2':
                result = subtract(num1, num2)
                op = '-'
            elif choice == '3':
                result = multiply(num1, num2)
                op = '*'
            elif choice == '4':
                result = divide(num1, num2)
                op = '/'
            print(f"\nResult: {num1} {op} {num2} = {result}")
        else:
            print("\n[Error] Invalid choice. Please select a valid option.")
