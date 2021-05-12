savedVariables = {}

def getVariable(name, line):
    if name in savedVariables:
        return savedVariables.get(name)
    else:
        print("Variable not initiated")
        print("Syntax error on line " + str(line) + "\n")
        raise SyntaxError
