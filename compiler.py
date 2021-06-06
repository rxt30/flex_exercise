import sys
import misc.executor as executor
import misc.treeBuilder as treeBuilder

from lexical.lexical import *
from syntax.syntax import *

fileinput = False

for names in sys.argv[1:]:
    if names == '-h':
        print('''
        Usage: python compiler.py [OPTION] [FILENAME]\n
        Options:    -h Shows this help menu\n
                    -f [file] File input\n
                    -v Verbose mode\n
                    -t Syntax Tree Output in Command Line\n
                    -i Syntax Tree Image in Browser''')
        exit(0)
    elif names == '-v':
        executor.verbose = True
    elif names == '-f':
        fileinput = True
    elif names == '-t':
        treeBuilder.showClTree = True
    elif names == '-i':
        treeBuilder.showBrowserTree = True



if not fileinput:
    while True:
        syntaxTree = parser.parse(input("Please enter something:\n"))
        executor.execute_tree(syntaxTree)
        treeBuilder.build_tree(syntaxTree)

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
    executor.execute_tree(syntaxTree)
    treeBuilder.build_tree(syntaxTree)
