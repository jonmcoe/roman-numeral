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
    :param x: positive integer > 1
    :return: return greatest power of 10 smaller than x
    """
    return 10**int(math.ceil(math.log(x, 10) - 1))


def convert(decimal_input):
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
