operations = {
    "1": ("sum", sum),
    "2": ("mean", lambda x: sum(x) / len(x)),
    "3": ("min", min),
    "4": ("max", max)
}

operations_text = "\n".join(f'{key} - {text}' for key, (text, _) in operations.items())

def calculator():
    """Gather a list of numbers from user input and calculate the operation"""
    numbers = []
    result = None

    # could be simplified by walrus operator in Python 3.8
    user_input = ""
    while user_input != 'q':
        user_input: str = input("Please enter any number that will be added to the list, or abort with 'q'.")

        try:
            number = float(user_input)
        except ValueError:
            print("Please enter a valid numerical value")
            continue
        
        numbers.append(number)
        print(f"Current list of numbers: {numbers}")

    user_input = ""
    while user_input not in operations:
        print("Available operations:\n", operations_text)
        user_input: str = input("Please specify the number for the operation you want to apply to the list of numbers.")

        if user_input not in operations:
            print("Please choose a valid option!")

    result = operations[user_input][1](numbers)

    print(f"The {operations[user_input][0]} of {numbers} is {result}.")

    return result


if __name__ == "__main__":
    calculator()