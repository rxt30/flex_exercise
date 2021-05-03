savedVariables = {}

def p_variable_int(p):
    'variable : INTEGER CHARS ASSIGNMENT expression'
    if type(p[4]) is not int:
        print("Wrong dataType")
        return
    savedVariables.update({p[2] : p[4]})
    print(savedVariables)

def p_variable_string(p):
    'variable : STRING CHARS ASSIGNMENT QUOTED_CHARS'
    if type(p[4]) is not str:
        print("Wrong dataType for Assignment")
        return
    savedVariables.update({p[2] : p[4].strip("'\"")})
    print(savedVariables)

def p_variable_bool(p):
    '''variable : BOOLEAN CHARS ASSIGNMENT TRUE
                | BOOLEAN CHARS ASSIGNMENT FALSE'''
    savedVariables.update({p[2] : p[4] == "true"})
    print(savedVariables)
