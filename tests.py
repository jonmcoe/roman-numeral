from unittest import TestCase

from roman_numeral import convert


cases = {
    1: 'I',
    3: 'III',
    4: 'IV',
    5: 'V',
    7: 'VII',
    10: 'X',
    11: 'XI',
    14: 'XIV',
    15: 'XV',
    19: 'XIX',
    50: 'L',
    83: 'LXXXIII',
    100: 'C',
    500: 'D',
    1000: 'M',
    1001: 'MI',
    1900: 'MCM',
    1987: 'MCMLXXXVII',
    50005: 50*'M'+'V',
}


class RomanNumeralTestCase(TestCase):
    pass


def make_function(decimal_input, roman_output):
    def _current(self):
        self.assertEquals(convert(decimal_input), roman_output)
    _current.__name__ = 'test_'+str(decimal_input)
    return _current

for k, v in cases.items():
    f = make_function(k, v)
    setattr(RomanNumeralTestCase, f.__name__, f)
