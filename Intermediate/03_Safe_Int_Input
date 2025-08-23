def read_int(prompt, min, max):
    """
    Safely read an integer from user input within a specified range.

    Parameters:
    prompt (str): The message displayed to the user when asking for input.
    min (int): The minimum acceptable value.
    max (int): The maximum acceptable value.

    Returns:
    int: A valid integer entered by the user within the range [min, max].
    
    Behavior:
    - Prompts the user until a valid integer within the range is entered.
    - If the user enters non-integer input, prints an error and asks again.
    - If the user enters a number outside the range, prints an error and asks again.
    """
    
    ok = False  # Boolean flag to control the input loop
    
    while not ok:
        try:
            # Ask for user input and attempt to convert to integer
            value = int(input(prompt))
            ok = True  # Input is a valid integer, proceed to range check
        except ValueError:
            # If input is not an integer, print error and repeat loop
            print("Error: wrong input")
        
        if ok:
            # Check if the integer is within the allowed range
            ok = value >= min and value <= max
        
        if not ok:
            # If integer is outside the range, inform the user
            print(f"Error: the value is not within permitted range ({min}..{max})")
    
    return value  # Return the valid integer


# Example usage of the function
v = read_int("Enter a number from -10 to 10: ", -10, 10)
print("The number is:", v)
