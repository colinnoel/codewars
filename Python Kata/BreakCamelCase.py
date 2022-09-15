# Complete the solution so that the function will break up camel casing, using a space between words.

# Example
# "camelCasing"  =>  "camel Casing"
# "identifier"   =>  "identifier"
# ""             =>  ""

import re

def solution(s):
    return re.sub('([A-Z])', r' \1', s)


s = "helloWorld"
print(solution(s))