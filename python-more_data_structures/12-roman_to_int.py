#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    dico = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = 0
    for i in range(len(roman_string)):
        if i > 0 and dico[roman_string[i]] > dico[roman_string[i - 1]]:
            num += dico[roman_string[i]] - 2 * dico[roman_string[i - 1]]
        else:
            num += dico[roman_string[i]]
    return num
