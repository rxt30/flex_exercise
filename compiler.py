import sys
from tokens.tokens import tokens
from lexical.lexical import *
from syntax.syntax import *
from executor import execute

if len(sys.argv) == 1:
    while True:
        syntaxTree = parser.parse(input("Please enter something:\n"))
        print(syntaxTree)
        for statement in syntaxTree:
            result = execute(statement)
            print(result)

else:
    f = open(sys.argv[1])
    content = f.readlines()
    code = ''
    for line in content:
        code += line
    syntaxTree = parser.parse(code)
    print(syntaxTree)
    for statement in syntaxTree:
        result = execute(statement)
        print(result)
