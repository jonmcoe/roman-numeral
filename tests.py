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
    50005: 50*'M'+'V'
}


class RomanNumeralTestCase(TestCase):

    def __init__(self, debug=False, *args, **kwargs):
        self.debug = debug
        for decimal_input, roman_output in cases.items():
            def _current(self):
                self.assertEquals(convert(decimal_input), roman_output)
            setattr(RomanNumeralTestCase, 'test_'+roman_output, _current)
        super(RomanNumeralTestCase, self).__init__(*args, **kwargs)

    def test_all(self):
        for decimal_input, roman_output in cases.items():
            self.assertEquals(convert(decimal_input), roman_output)

    def runTest(self):
        for test_method_name in [i for i in dir(self) if i.startswith('test')]:
            test_method = getattr(self, test_method_name)
            if callable(test_method):
                test_method()
                print("passed " + test_method_name)
