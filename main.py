#!/usr/bin/python3
"""
#Hacktoberfest 2017
This will take input and rot13 the input.
"""

def rot13():
    import string

    alphabet = string.ascii_lowercase
    text = input("Rot 13 Text:\n").lower()
    rotated = []

    for letter in text:
        if letter.isalpha():
            position = alphabet.find(letter)

            if position < 13:
                new_letter = alphabet[position + 13]
                rotated.append(new_letter)
            elif position >= 13:
                new_letter = alphabet[position - 13]
                rotated.append(new_letter)

        else:
            new_letter = letter
            rotated.append(new_letter)

    print()
    print("Old:\t" + text)
    print("New:\t" + ''.join(rotated))

rot13()
