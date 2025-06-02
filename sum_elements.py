import sys

#A poorly written example of a program in Python. It prompts the user for the number of elements to sum, takes those integers as input, and handles some basic error cases

MAX_ELEMENTS = 100

def calculate_sum(numbers):
    """
    Calculates the sum of all elements in the given iterable.

    Args:
        numbers (iterable): An iterable of numbers to be summed.

    Returns:
        int or float: The sum of all elements in the iterable.
    """
    return sum(numbers)

def get_integer(prompt, min_value=None, max_value=None):
    """
    Prompts the user for an integer input, with optional range validation.

    Args:
        prompt (str): The prompt message to display.
        min_value (int, optional): Minimum acceptable value.
        max_value (int, optional): Maximum acceptable value.

    Returns:
        int: The validated integer input from the user.
    """
    while True:
        try:
            value = int(input(prompt))
            if (min_value is not None and value < min_value) or \
               (max_value is not None and value > max_value):
                print(f"Please enter a value between {min_value} and {max_value}.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def main():
    try:
        n = get_integer(f"Enter the number of elements (1-{MAX_ELEMENTS}): ", 1, MAX_ELEMENTS)
        numbers = []
        print(f"Enter {n} integers:")
        for i in range(n):
            num = get_integer(f"Element {i+1}: ")
            numbers.append(num)
        total = calculate_sum(numbers)
        print("Sum of the numbers:", total)
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")

if __name__ == "__main__":
    main()
