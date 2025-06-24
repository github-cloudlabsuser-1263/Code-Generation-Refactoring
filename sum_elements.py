# A refactored version of the program that is more readable, has better input validation, improved prompts, and follows best practices. It uses loops for input validation and avoids using exit().

MAX_ELEMENTS = 100

def calculate_sum(numbers):
    return sum(numbers)

def get_integer(prompt, min_value=None, max_value=None):
    while True:
        try:
            value = int(input(prompt))
            if (min_value is not None and value < min_value) or (max_value is not None and value > max_value):
                print(f"Please enter a value between {min_value} and {max_value}.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def main():
    print("=== Sum Elements Program ===")
    n = get_integer(f"Enter the number of elements (1-{MAX_ELEMENTS}): ", 1, MAX_ELEMENTS)
    numbers = []
    for i in range(1, n + 1):
        num = get_integer(f"Enter integer #{i}: ")
        numbers.append(num)
    total = calculate_sum(numbers)
    print("Sum of the numbers:", total)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
