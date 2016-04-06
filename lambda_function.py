from roman_numeral import convert_to_decimal, convert_to_roman
# ---

import logging

logger = logging.getLogger()


def lambda_handler(event, context, *args, **kwargs):
    if not event.get('value'):
        return None

    input_value = event['value']
    input_value = input_value if isinstance(input_value, basestring) else str(input_value)
    # default output is roman string. it is decimal iff either:
    #   1) explicitly specified in POST body's `output_to_decimal` field
    #   2) or input is pure alphabetic (otherwise roman output would be identical to input, which seems undesirable)
    output_to_decimal = event.get('output_to_decimal', input_value.isalpha())

    try:
        # extremely half-ass (quarter-ass?) parsing
        initial_chunks = input_value.split(' ') # must have spaces between operators
        formatter = lambda x: str(convert_to_decimal(x.strip())) if x.isalpha() else x
        chunks = map(formatter, initial_chunks)
        final_string = ''.join(chunks)
        ans = eval(final_string)  # unsafe? sure. but it's ok bc its an AWS lambda

        return ans if output_to_decimal else convert_to_roman(ans)
    except Exception:
        logger.exception("Original: {0}, Translated: {1}".format(
            input_value, locals().get('final_string', 'unreachable')
        ))
        return "Bad format"
