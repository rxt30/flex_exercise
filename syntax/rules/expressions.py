def p_expression_plus(p):
    'expression : expression PLUS term'
    p[0] = p[1] + p[3]

def p_expression_minus(p):
    '''expression : expression MINUS term
                | MINUS term'''
    if len(p) == 4:
        p[0] = p[1] - p[3]
    else:
        p[0] = -1*p[2]

def p_expression_braces(p):
    'expression : ROUND_START expression ROUND_END'
    p[0] = (p[2])

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_expression_variable(p):
    'expression : variable'
    p[0] = p[1]

def p_expression_int(p):
    'expression : INTEGER'
    print("I am a int")
