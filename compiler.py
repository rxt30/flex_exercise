import sys

from executor import execute_tree
from tokens.tokens import tokens
from lexical.lexical import *
from syntax.syntax import *

if len(sys.argv) == 1:
    while True:
        syntaxTree = parser.parse(input("Please enter something:\n"))
        print('Syntax-Tree: ' + str(syntaxTree))
        execute_tree(syntaxTree)
else:
    f = open(sys.argv[1])
    content = f.readlines()
    code = ''
    for line in content:
        code += line
    syntaxTree = parser.parse(code)
    print('Syntax-Tree: ' + str(syntaxTree))
    execute_tree(syntaxTree)
