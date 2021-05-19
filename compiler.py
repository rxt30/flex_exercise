import sys
from tokens.tokens import tokens
from lexical.lexical import *
from syntax.syntax import *

if len(sys.argv) == 1:
    while True:
        result = parser.parse(input("Please enter something:\n"))
        print(result)

else:
    f = open(sys.argv[1])
    content = f.readlines()
    code = ''
    for line in content:
        code += line
    result = parser.parse(code)
    print(result)