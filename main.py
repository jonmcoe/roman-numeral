import string
import sys

from roman_numeral import convert_to_decimal, convert_to_roman

arg = sys.argv[1] if len(sys.argv) > 1 else sys.stdin.readline().rsplit(" ", 1)[0].strip()

if all([c in string.digits for c in arg]):
    print(convert_to_roman(int(arg)))

elif all([c in string.letters for c in arg]):
    print(convert_to_decimal(arg))
