import sys
import executor

from lexical.lexical import *
from syntax.syntax import *

for names in sys.argv[1:]:
    if names == '-h':
        print('''
        Usage: python compiler.py [OPTION] [FILENAME]\n
        Options:    -h Shows this help menu\n
                    -v Verbose mode''')
        exit(0)
    elif names == '-v':
        executor.verbose = True

if len(sys.argv) == 1 or (executor.verbose and len(sys.argv) == 2):
    while True:
        syntaxTree = parser.parse(input("Please enter something:\n"))
        if executor.verbose:
            print('Syntax-Tree: ' + str(syntaxTree))
        executor.execute_tree(syntaxTree)

else:
    for names in sys.argv[1:]:
        try:
            f = open(names)
            content = f.readlines()
            break
        except:
            pass

    if not content:
        print("Invalid file delivered")
        exit(1)

    code = ''
    for line in content:
        code += line
    syntaxTree = parser.parse(code)
    if executor.verbose:
        print('Syntax-Tree: ' + str(syntaxTree))
    executor.execute_tree(syntaxTree)
