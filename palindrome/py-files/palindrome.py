# **************************** Challenge: Palindrome ****************************
"""
Author: Trinity Terry
pyrun: python palindrome.py
"""
# Write a function that tests whether a string is a palindrome.
def is_palindrome(string):
    '''
    Checks to see is passed in string is a palindrome

    string -- string

    Returns: Boolean
    '''

    if type(string) != str:
        raise TypeError("is_palindrome only takes string arguments")
    else:
        no_whitespace = [char.lower() for char in string if char.isalpha()]
        hold_bool = list()
        for i in reversed(range(len(no_whitespace))):
            hold_bool.append(no_whitespace[-i - 1] == no_whitespace[i])
        return False in hold_bool

print(is_palindrome("here"))
print(is_palindrome("This is a Sentence"))
print(is_palindrome("No lemon, no melon"))
print(is_palindrome("Eva, can I see bees in a cave?"))
