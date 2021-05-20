#savedVariables = {}
from syntax.rules.savedVariables import savedVariables

def p_variable_int(p):
    '''variable : INTEGER CHARS ASSIGNMENT expression'''
    if type(p[4]) is not float:
        wrong_assignment_error(p)
    savedVariables.update({p[2] : int(p[4])})
    print(savedVariables)

def p_variable_float(p):
    'variable : FLOAT CHARS ASSIGNMENT expression'
    if type(p[4]) is not float:
        wrong_assignment_error(p)
    savedVariables.update({p[2] : float(p[4])})
    print(savedVariables)

def p_variable_string(p):
    'variable : STRING CHARS ASSIGNMENT expression'
    if type(p[4]) is not str:
        wrong_assignment_error(p)
    savedVariables.update({p[2] : p[4].strip("'\"")})
    print(savedVariables)

def p_variable_bool(p):
    '''variable : BOOLEAN CHARS ASSIGNMENT TRUE
                | BOOLEAN CHARS ASSIGNMENT FALSE'''
    savedVariables.update({p[2] : p[4] == "true"})
    print(savedVariables)

def p_variable_varConcat(p):
    'variable : CHARS ASSIGNMENT expression'
    if not (p[1] in savedVariables and type(p[3]) == type(savedVariables[p[1]])):
        wrong_reassignment_error(p)

    savedVariableType = type(savedVariables[p[1]])
    if savedVariableType is str:
        savedVariables.update({p[1] : p[3].strip("'\"")})
    elif savedVariableType is int:
        savedVariables.update({p[1] : p[3]})

    print(savedVariables)

def p_variable_reassign_bool(p):
    '''variable : CHARS ASSIGNMENT TRUE
                | CHARS ASSIGNMENT FALSE'''
    if not (p[1] in savedVariables and type(savedVariables[p[1]]) is bool):
        wrong_reassignment_error(p)
    savedVariables.update({p[1] : p[3] == "true"})
    print(savedVariables)


def wrong_assignment_error(p):
    print("Wrong dataType for assignment")
    print("Syntax error on line " + str(p.lineno(1)) + "\n")
    raise SyntaxError

def wrong_reassignment_error(p):
    print("Wrong dataType for reassignment")
    print("Syntax error on line " + str(p.lineno(1)) + "\n")
    raise SyntaxError
