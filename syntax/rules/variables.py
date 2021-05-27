#savedVariables = {}
import executor
from syntax.rules.savedVariables import savedVariables

def p_variable_int(p):
    'variable : INTEGER CHARS ASSIGNMENT expression'
    p[0] = ['ASSIGNMENT_INT', p[2], p[4], p.lineno(1)]

def p_variable_float(p):
    'variable : FLOAT CHARS ASSIGNMENT expression'
    p[0] = ['ASSIGNMENT_FLOAT', p[2], p[4], p.lineno(1)]

def p_variable_string(p):
    'variable : STRING CHARS ASSIGNMENT expression'
    p[0] = ['ASSIGNMENT_STRING', p[2], p[4], p.lineno(1)]

def p_variable_bool(p):
    'variable : BOOLEAN CHARS ASSIGNMENT condition'
    p[0] = ['ASSIGNMENT_BOOL', p[2], p[4], p.lineno(1)]

def p_variable_varConcat(p):
    'variable : CHARS ASSIGNMENT expression'
    p[0] = ['REASSIGNMENT', p[1], p[3], p.lineno(1)]

def p_variable_reassign_bool(p):
    '''variable : CHARS ASSIGNMENT TRUE
                | CHARS ASSIGNMENT FALSE'''
    if not (p[1] in savedVariables and type(savedVariables[p[1]]) is bool):
        wrong_reassignment_error(p)
    savedVariables.update({p[1] : p[3] == "true"})
    print(savedVariables)


# def wrong_assignment_error(p):
#     print("Wrong dataType for assignment")
#     print("Syntax error on line " + str(p.lineno(1)) + "\n")
#     raise SyntaxError

def wrong_reassignment_error(p):
    print("Wrong dataType for reassignment")
    print("Syntax error on line " + str(p.lineno(1)) + "\n")
    raise SyntaxError
