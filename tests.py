from unittest import TestCase

from nose_parameterized import parameterized

from roman_numeral import convert


TEST_PARAMS = [
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
        testcase_func_name=lambda func_name, _, params: 'test_{0}_is_{1}'.format(*params.args)
    )
    def test_(self, decimal, roman):
        self.assertEquals(convert(int(decimal)), roman)