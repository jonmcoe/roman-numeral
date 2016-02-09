DECIMAL_TO_ROMAN = {
    1000: ('M', 100),
    500: ('D', 100),
    100: ('C', 10),
    50: ('L', 10),
    10: ('X', 1),
    5: ('V', 1),
    1: ('I', None)
}


def convert(decimal_input):
    if decimal_input == 0:
        return ''

    ans = ''
    for current in sorted(DECIMAL_TO_ROMAN.keys(), reverse=True):
        current_roman, eligible_prefix = DECIMAL_TO_ROMAN[current]

        if decimal_input >= current:
            x = (decimal_input // current)
            decimal_input -= (current * x)
            ans += x * current_roman

        if eligible_prefix and decimal_input >= current - eligible_prefix:
            decimal_input -= (current - eligible_prefix)
            eligible_prefix_roman = DECIMAL_TO_ROMAN[eligible_prefix][0]
            ans += eligible_prefix_roman + current_roman
    return ans
