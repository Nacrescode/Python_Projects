"""
Four Sample Programs + Sudoku Validator
This script contains:
1. Palindrome checker
2. Anagram checker
3. Digit of Life calculator
4. Find a Word game
5. Sudoku validator
"""

def palindrome():
    """Check if a string is a palindrome (ignores spaces and case)."""
    pl = input("Please enter a string: ").lower().replace(" ", "")
    r_pl = pl[::-1]

    if pl == "" or pl != r_pl:
        print("It's not a palindrome")
    else:
        print("It's a palindrome")


def anagram():
    """Check if two strings are anagrams (ignores spaces and case)."""
    pl1 = input("Please enter the first string: ").lower().replace(" ", "")
    pl2 = input("Please enter the second string: ").lower().replace(" ", "")

    if sorted(pl1) != sorted(pl2) or pl1 == "":
        print("Not anagrams")
    else:
        print("Anagrams")


def digit_of_life():
    """Calculate the Digit of Life from birthday (YYYYMMDD, DDMMYYYY, etc.)."""
    bd = input("Please enter your birthday in DDMMYYYY format (e.g., 15031990): ").strip()

    while len(bd) > 1:   # Reduce to single digit
        total = 0
        for i in bd:
            total += int(i)
        bd = str(total)

    print("Your Digit of Life is:", bd)


def find_word():
    """Check if all letters of the first word appear in order in the second string."""
    word = input("Enter the word you wish to find: ").upper()
    strn = input("Enter the string you wish to search through: ").upper()

    found = True
    start = 0

    for i in word:
        pos = strn.find(i, start)
        if pos == -1:
            found = False
            break
        else:
            start = pos + 1

    if found:
        print("Yes")
    else:
        print("No")


def sudoku_validator():
    """Validate a Sudoku grid (rows, columns, and 3x3 sub-squares)."""
    def checkset(digs):
        """Check if set contains exactly digits 1–9."""
        return set(digs) == set("123456789")

    rows = []

    # Input rows
    for i in range(9):
        rowi = input("Please enter a nine-digit number: ")
        while len(rowi) != 9 or not rowi.isdigit():
            print("Invalid input! Please enter exactly 9 digits.")
            rowi = input("Please enter a NINE-DIGIT number: ")
        rows.append(rowi)

    # Check all rows
    for row in rows:
        if not checkset(row):
            print("No")
            return

    # Check all columns
    for i in range(9):
        col = [row[i] for row in rows]
        if not checkset(col):
            print("No")
            return

    # Check all 3x3 sub-squares
    for r in range(0, 9, 3):
        for c in range(0, 9, 3):
            sqr = []
            for i in range(3):
                sqr.extend(rows[r+i][c:c+3])
            if not checkset(sqr):
                print("No")
                return

    # If all tests passed
    print("Yes")


def main():
    """Main menu for choosing which program to run."""
    print("Select a program to run:")
    print("1. Palindrome checker")
    print("2. Anagram checker")
    print("3. Digit of Life calculator")
    print("4. Find a Word game")
    print("5. Sudoku validator")

    choice = input("Enter a number (1-5): ").strip()

    if choice == "1":
        palindrome()
    elif choice == "2":
        anagram()
    elif choice == "3":
        digit_of_life()
    elif choice == "4":
        find_word()
    elif choice == "5":
        sudoku_validator()
    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()
