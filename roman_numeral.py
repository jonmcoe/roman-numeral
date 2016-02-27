import math


DECIMAL_TO_ROMAN = {
    1000: 'M',
    500: 'D',
    100: 'C',
    50: 'L',
    10: 'X',
    5: 'V',
    1: 'I'
}


def get_prefix(x):
    """
    :param x: positive integer
    :return: return greatest power of 10 smaller than x if x > 1. else None
    """
    return 10**int(math.ceil(math.log(x, 10) - 1)) if x > 1 else None


roman_to_decimal = {}

for decimal, roman in DECIMAL_TO_ROMAN.items():
    roman_to_decimal[roman] = decimal
    possible_prefix_decimal = get_prefix(decimal)
    if possible_prefix_decimal:
        prefix_roman = DECIMAL_TO_ROMAN[possible_prefix_decimal]
        roman_to_decimal[prefix_roman + roman] = decimal - possible_prefix_decimal


def convert_to_roman(decimal_input):
    if decimal_input == 0:
        return ''

    ans = ''
    for current in sorted(DECIMAL_TO_ROMAN.keys(), reverse=True):
        current_roman = DECIMAL_TO_ROMAN[current]
        eligible_prefix = get_prefix(current)

        if decimal_input >= current:
            x = (decimal_input // current)
            decimal_input -= (current * x)
            ans += x * current_roman

        if eligible_prefix and decimal_input >= current - eligible_prefix:
            decimal_input -= (current - eligible_prefix)
            eligible_prefix_roman = DECIMAL_TO_ROMAN[eligible_prefix]
            ans += eligible_prefix_roman + current_roman
    return ans


def convert_to_decimal(roman_input):

    if len(roman_input) > 1 and roman_to_decimal[roman_input[0]] < roman_to_decimal[roman_input[1]]:
        return roman_to_decimal[roman_input[:2]] + convert_to_decimal(roman_input[2:])

    return roman_to_decimal[roman_input[0]] + convert_to_decimal(roman_input[1:]) if roman_input else 0