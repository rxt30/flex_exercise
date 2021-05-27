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
