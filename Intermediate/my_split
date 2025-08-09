"""
mysplit function: A custom implementation of Python's built-in split() method.
This function takes a string and returns a list of words, separated by spaces.
It works without using the built-in split() method.

Features:
- Handles empty strings.
- Handles strings with only whitespace.
- Keeps multiple spaces between words from creating empty list elements.
"""

def mysplit(strng):
    """
    Splits the given string into words without using str.split().

    Args:
        strng (str): The string to be split.

    Returns:
        list: A list containing words from the string.
    """
    mylist = []  # List to store the words
    word = ""    # Temporary variable to build each word

    # Check if the string is empty or contains only spaces
    if not strng or strng.isspace():
        return mylist

    # Iterate through each character in the string
    for i in strng:
        if i != " ":
            # Add non-space characters to the current word
            word += i
        else:
            # If a space is found and word is not empty, append it to the list
            if word != "":
                mylist.append(word)
                word = ""  # Reset word to start collecting the next one

    # Append the last word if there is one
    if word != "":
        mylist.append(word)

    return mylist


# Test cases
print(mysplit("To be or not to be, this is a question"))
print(mysplit("To be or not to be,this is a question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))

