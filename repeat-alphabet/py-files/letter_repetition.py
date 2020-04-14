# **************************** Challenge: Repeat the Alphabet ****************************
"""
Author: Trinity Terry
pyrun: python letter_repetition.py
"""
import string

# Write a function called alpha_repeat that takes one argument. 
def alpha_repeat(argument):
    """
    Construct an output that vertically repeats each character in the string. The number of times a letter is repeated depends on its position in the alphabet. Assume it's 0-indexed: so A is at index position 0 and would therefore be repeated 0 times, b is at index position 1 and would be repeated 1 time, and so on.

    argument -- string: If a character is not a letter, It will be remoed from the string. 

    Returns: 
    """
    # If this argument is not a string, raise an exception that informs the user that this function needs an argument of type string.
    if type(argument) != str:
        raise TypeError("argument passed to alpha_repeat needs to be a string")
    else:
        # If the argument is a string, make sure the string only contains letters of the alphabet. Any numbers, symbols etc. should be removed from the string.

        only_letters = "".join([char for char in argument if char.isalpha()])
        # Use your string to construct an output which vertically repeats each character in the string. The number of times a letter is repeated depends on its position in the alphabet. Assume it's 0-indexed: so A is at index position 0 and would therefore be repeated 0 times, b is at index position 1 and would be repeated 1 time, and so on.
        # Creates list the alphabet

        alphabet = list(string.ascii_lowercase)
        for i in range(len(alphabet)):
            print(only_letters)
            only_letters = "".join(map(lambda char: do_letters_match(char, alphabet[i]), only_letters))

            if not only_letters.strip():
                break

def do_letters_match(let_1, let_2):
    if let_1.lower() == let_2:
        return " "
    else:
        return let_1

alpha_repeat("Hello There My name is Trinity")