from syntax.rules.savedVariables import *

def p_term_multiplication(p):
    'term : term MULTIPLICATION term'
    p[0] = p[1] * p[3]

def p_term_expression(p):
    'term : ROUND_START expression ROUND_END MULTIPLICATION term'
    p[0] = (p[2]) * p[5]

def p_term_expression_single(p):
    'term : ROUND_START expression ROUND_END'
    p[0] = (p[2])

def p_term_number(p):
    '''term : NUMBER
            | MINUS NUMBER'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = -1*p[2]

def p_term_chars(p):
    'term : QUOTED_CHARS'
    p[0] = p[1].strip("\"'")

def p_term_variable(p):
    'term : CHARS'
    p[0] = getVariable(p[1], p.lineno(1))
