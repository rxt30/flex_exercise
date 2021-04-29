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
    for line in content:
        print(line, end="")
        parsed_line = parser.parse(line)
        if parsed_line is not None:
            print("parsed to " + str(parsed_line) + "\n")
