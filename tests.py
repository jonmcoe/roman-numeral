from unittest import TestCase

from nose_parameterized import parameterized

from roman_numeral import convert_to_decimal, convert_to_roman


TEST_PARAMS = [
    (0, ''),
    (1, 'I'),
    (3, 'III'),
    (4, 'IV'),
    (5, 'V'),
    (7, 'VII'),
    (10, 'X'),
    (11, 'XI'),
    (14, 'XIV'),
    (15, 'XV'),
    (19, 'XIX'),
    (50, 'L'),
    (100, 'C'),
    (83, 'LXXXIII'),
    (500, 'D'),
    (1000, 'M'),
    (1001, 'MI'),
    (1900, 'MCM'),
    (1987, 'MCMLXXXVII'),
    (50005, 50*'M' + 'V'),
]


class RomanNumeralTestCase(TestCase):

    @parameterized.expand(
        TEST_PARAMS,
        testcase_func_name=lambda func_name, _, params: 'test_decimal{0}_is_roman{1}'.format(*params.args)
    )
    def test_decimal_to_roman(self, decimal, roman):
        self.assertEquals(convert_to_roman(decimal), roman)

    @parameterized.expand(
        TEST_PARAMS,
        testcase_func_name=lambda func_name, _, params: 'test_roman{0}_is_decimal{1}'.format(*params.args)
    )
    def test_decimal_to_roman(self, decimal, roman):
        self.assertEquals(convert_to_decimal(roman), decimal)

    def test_bad_string_raises_value_error(self):
        with self.assertRaises(ValueError):
            convert_to_decimal('phish')

    def test_lowercase_ok(self):
        self.assertEquals(convert_to_decimal('v'), 5)
