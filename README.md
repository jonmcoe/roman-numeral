# Caesar Calc
Deployed at https://caesarcalc.com

## Core logic
`roman_numeral.py` has all of it. Two functions: `convert_to_roman` and `convert_to_decimal`

Tests are in `tests.py` and require the packages in `test_requirements.txt`

Super-minimal commandline usage with `main.py`

## API
AWS Lambda and API Gateway. Contents of lambda function in file `lambda_function.py`

POST to `https://a0p25chmzl.execute-api.us-east-1.amazonaws.com/prod` 

Request:
```json
{
    "value": "X ** 2 - 5 + CXI"
}
```

Response:
```json
{
    "roman": "CCVI",
    "decimal": 206
}
```

Errors look like this.
Request:
```json
{
    "value": "suh dude"
}
```
Response:
```json
{
    "errorMessage": "Bad format"
}
```

Note that **all** responses have status code of 200.

String evaluates with a python `eval` (after converting roman tokens to decimal)so all python operations (+, -, *, /, **) 
should be fair game. You can even do stuff like `sum( [ 982, v , x ** iii ] )`
Note that roman numerals need to have spaces on either side. `X+5` or `(v + 7) ** 2` are not OK, but `X + 5` and `( v + 7) ** 2` should be.

## Website
Exact contents of web folder are served as an S3 Static Website. Route 53 --> CloudFront --> S3

It's all in `web/index.html` right now. Uses only jquery. Mobile UX is just ok.

Presents an input and sends to API on keypress as long as an (incomplete) client-side validation passes.
Two outputs for the decimal and roman portions of response JSON. Or for the error message.


## TODOs
1. API Gateway response code
    * Need to write rules into API Gateway so error responses have a 4xx status code, and update website accordingly
1. Investigate existing roman numeral related libraries on PyPi and see if my code can be replaced.
1. A better front-end thru React/Redux and real build tools.
1. Domain name for API
    * Website is served thru Cloudfront and Route53, thus the pretty URL (and certificate)
    * API is still using ugly API Gateway "execute-api.us-east-1.amazonaws.com" URL. Would like `api.caesarcalc.com`
1. Many invalid roman numerals convert without error, but not necessarily sanely.
    * `convert_to_decimal('iiiii')` == `5`, that's ok i guess.
    * `convert_to_decimal('ixixcixi')` == `128`, that's kinda weird
1. Actually parse incoming strings responsibly instead of using eval crutch