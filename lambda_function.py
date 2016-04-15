from roman_numeral import convert_to_decimal, convert_to_roman
# ---

import logging

logger = logging.getLogger()


def lambda_handler(event, context):
    context = None  # we don't use it, and don't want to potentially expose in the eval below
    if not event.get('value'):
        return None

    input_value = event['value']
    input_value = input_value if isinstance(input_value, basestring) else str(input_value)

    try:
        # extremely half-ass (quarter-ass?) parsing
        initial_chunks = input_value.split(' ')  # must have spaces between operators and roman characters
        formatter = lambda x: str(convert_to_decimal(x.strip())) if x.isalpha() else x
        chunks = map(formatter, initial_chunks)
        final_string = ''.join(chunks)
        ans = eval(final_string)  # unsafe? sure. but it's ok bc its an AWS lambda and not a "real" machine

        return {
            "roman": convert_to_roman(ans),
            "decimal": ans
        }
    except Exception as e:
        logger.exception("Original: {0}, Translated: {1}".format(
            input_value, locals().get('final_string', 'unreachable')
        ))
        raise e.__class__("Bad Request: " + e.__class__.__name__ + ' w/ ' + e.message)
