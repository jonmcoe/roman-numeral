import sys

from roman_numeral import convert
from tests import RomanNumeralTestCase

test_case = RomanNumeralTestCase(debug=True)
test_case.runTest()

print(convert(int(sys.argv[1])))