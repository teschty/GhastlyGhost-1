#!/usr/bin/python3
import argparse
import string

parser = argparse.ArgumentParser(description='ROT13')
parser.add_argument('string', metavar='string', type=str, nargs='+', help='rot 13 for alphabet only chars.')
# parser.add_argument('-l', metavar='lowercase', type=str, nargs='+', help='make lowercase.')
# parser.add_argument('-u', metavar='uppercase', type=str, nargs='+', help='make uppercase.')

args = parser.parse_args()
text = args.string

alphabet = string.ascii_lowercase
print(text)
print(alphabet)
