savedVariables = {}

def p_variable_int(p):
    'variable : INTEGER CHARS ASSIGNMENT expression'
    if type(p[4]) is not int:
        print("Wrong dataType")
        print("Syntax error on line " + str(p.lineno(1)) + "\n")
        raise SyntaxError
    savedVariables.update({p[2] : p[4]})
    print(savedVariables)

def p_variable_string(p):
    'variable : STRING CHARS ASSIGNMENT QUOTED_CHARS'
    if type(p[4]) is not str:
        print("Wrong dataType for Assignment")
        print("Syntax error on line " + str(p.lineno(1)) + "\n")
        raise SyntaxError
    savedVariables.update({p[2] : p[4].strip("'\"")})
    print(savedVariables)

def p_variable_bool(p):
    '''variable : BOOLEAN CHARS ASSIGNMENT TRUE
                | BOOLEAN CHARS ASSIGNMENT FALSE'''
    savedVariables.update({p[2] : p[4] == "true"})
    print(savedVariables)

def p_variable_reassign(p):
    '''variable : CHARS ASSIGNMENT expression
                | CHARS ASSIGNMENT QUOTED_CHARS
                | CHARS ASSIGNMENT TRUE
                | CHARS ASSIGNMENT FALSE'''
    if p[1] in savedVariables and type(p[3]) == type(savedVariables[p[1]]):
        savedVariables.update({p[1] : p[3]})
    else:
        print("Wrong dataType for reassignment")
        print("Syntax error on line " + str(p.lineno(1)) + "\n")
        raise SyntaxError
    print(savedVariables)
