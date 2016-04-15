mkdir -p lambda_builds
zip -r ./lambda_builds/lambda-$(date -u +"%Y%m%dT%H%M%S")-$(git rev-parse HEAD).zip ./lambda_function.py ./roman_numeral.py