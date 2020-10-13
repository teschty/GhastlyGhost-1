#!/usr/bin/python3
"""
#Hacktoberfest 2017
This can take input and perform various operations. 
"""

import argparse


# Basic. Not very correct.
def pig_latin(text):
    pig_word = []
    for word in text:
        pig_word.append(word[1:].lower() + "-" + word[0].lower() + "ay")

    print("Old:\t" + ' '.join(text).lower())
    print("New:\t" + ' '.join(pig_word))


def rot13(text):
    import string

    # alphabet of lowercase chars
    alphabet = string.ascii_lowercase

    rotated = []
    for letter in text:
        if letter.isalpha():
            position = alphabet.find(letter)
            # rotate letters forward
            if position < 13:
                new_letter = alphabet[position + 13]
                rotated.append(new_letter)
            # rotate letters backwards
            elif position >= 13:
                new_letter = alphabet[position - 13]
                rotated.append(new_letter)
        else:
            # handles not alpha chars.
            new_letter = letter
            rotated.append(new_letter)

    print("Old:\t" + text)
    print("New:\t" + ''.join(rotated))


def palindrome(text):
    if text == text[::-1]:
        print('"{}" is a palindrome!'.format(text))
    else:
        print('"{}" is not a palindrome.'.format(text))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="manipulate text", epilog="cmd [-flag] [text]")

    # Force user to only do one thing at a time.
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-r13", "--rot13", type=str, nargs='*', help='Rotate 13')
    group.add_argument("-pal", "--palindrome", type=str, nargs='*', help='Same forwards as is backwards')
    group.add_argument("-pig", "--pig-latin", type=str, nargs='*', help='Basic Pig Latin')

    args = parser.parse_args()

    if args.pig_latin:
        pig_latin(args.pig_latin)
    elif args.rot13:
        text = ' '.join(args.rot13).lower()
        rot13(text)
    elif args.palindrome:
        text = ' '.join(args.palindrome).lower()
        palindrome(text)
    else:
        print("run this command with -h for help")
        print("run this command with a flag to specify a text transformation")


