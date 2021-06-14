from roman_numeral import convert_to_decimal, convert_to_roman
# ---
import json
import logging

logger = logging.getLogger()


class MissingRequiredParameterException(Exception):

    def __init__(self, missing_params):
        self.message = "Missing required parameters: {0}".format(', '.join(list(missing_params)))
        super(MissingRequiredParameterException, self).__init__()


def lambda_handler(event, context):
    context = None  # we don't use it, and don't want to potentially expose in the eval below
    REQUIRED_PARAMS = {'value'}
    missing_params = REQUIRED_PARAMS - set(event.keys())

    try:
        if missing_params:
            input_value = json.dumps(event)
            raise MissingRequiredParameterException(missing_params)

        input_value = event['value']
        input_value = input_value if isinstance(input_value, str) else str(input_value)

        # extremely half-ass (quarter-ass?) parsing
        initial_chunks = input_value.split(' ')  # must have spaces between operators and roman characters
        formatter = lambda x: str(convert_to_decimal(x.strip())) if x.isalpha() else x
        chunks = map(formatter, initial_chunks)
        final_string = ''.join(chunks)
        ans = eval(final_string) or 0  # unsafe? sure. but it's ok bc its an AWS lambda and not a "real" machine

        return {
            "roman": convert_to_roman(ans),
            "decimal": ans
        }
    except Exception as e:
        logger.exception("Original: {0}, Translated: {1}".format(
            input_value, locals().get('final_string', 'unreachable')
        ))
        raise Exception("Bad Request: " + e.__class__.__name__ + ' w/ ' + str(e))

