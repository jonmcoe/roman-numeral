from roman_numeral import convert_to_decimal, convert_to_roman
# ---

import logging

logger = logging.getLogger()


def lambda_handler(event, context, *args, **kwargs):
    if not event.get('value'):
        return None

    input_value = event['value']
    input_value = input_value if isinstance(input_value, basestring) else str(input_value)
    try:
        to_roman = not input_value.isalpha()

        initial_chunks = input_value.split(' ') # must have spaces between operators
        formatter = lambda x: str(convert_to_decimal(x.strip())) if x.isalpha() else x
        chunks = map(formatter, initial_chunks)
        final_string = ''.join(chunks)
        ans = eval(final_string)
        return convert_to_roman(ans) if to_roman else ans
    except Exception:
        logger.exception("")
        return "Bad format"
