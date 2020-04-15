# **************************** Challenge: English to Morse Code ****************************
"""
Author: Trinity Terry
pyrun: python english_morse.py
"""

# Write a program that automatically converts English text to Morse code and vice versa.
from morse_tree import start


def morse_code(string):
    '''
    Converts String to morse code
    '''

    available_char = ["?", ".", "-"]
    morse_word = list()
    string_word = list()
    key_list = ["", "", "", "", ""]
    lower_string = string.lower()
    has_letters = lower_string.islower()
    key_index = 1 if has_letters else 0

    # morse_index = 0 if string.islower() else 0

    def append_to_morse(letter, num):
        new_morse = list()
        for i in range(num):
            new_morse.append(key_list[i])
        morse_word.append("".join(new_morse))

    def append_to_string(letter, num):
        new_morse = list()
        for i in range(num):
            new_morse.append(key_list[i])
        string_word.append("".join(new_morse))

    if type(string) == str and has_letters:
        for i in range(len(string)):
            ch = string[i].lower() 
            if ch.isalpha() or ch in available_char or ch.isdigit():
                for (k1, v1) in start.items():
                    key_list[0] = k1[key_index]
                    if k1[0] == ch:
                        append_to_morse(ch, 1)
                    else:
                        for (k2, v2) in v1.items():
                            key_list[1] = k2[key_index]
                            print(key_list)
                            if k2[0] == ch:
                                append_to_morse(ch, 2)
                            else:
                                
                                for (k3, v3) in v2.items():
                                    key_list[2] = k3[key_index]
                                    if k3[0] == ch:
                                        append_to_morse(ch, 3)
                                    else:
                                        
                                        for (k4, v4) in v3.items():
                                            key_list[3] = k4[key_index]
                                            if k4[0] == ch:
                                                append_to_morse(ch, 4)
                                            else:
                                                if type(v4) == dict:
                                                    for (k5, v5) in v4.items():
                                                        key_list[4] = k5[key_index]
                                                        if k5[0] == ch:
                                                            append_to_morse(ch, 5)
            else:
                special = ([",", "--··--"],[" ", "     "])
                for item in special:
                    if item[0] == ch:
                        morse_word.append(item[1])

                morse_word.append(" ")

        return " ".join(morse_word) if has_letters else string_word
    else:
        raise TypeError(f"morse_code only accepts a string that contains letters as a argument")

print(morse_code("SOS"))
