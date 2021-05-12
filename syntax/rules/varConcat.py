from syntax.rules.savedVariables import *

def p_varConcat_plus(p):
    'varConcat : varConcat PLUS varConcat'
    p[0] = p[1] + p[3]

def p_varConcat_chars(p):
    'varConcat : CHARS'
    p[0] = getVariable(p[1], p.lineno(1))

def p_varConcat_expression(p):
    'varConcat : expression'
    p[0] = p[1]

def p_varConcat_plus_expression_pre(p):
    'varConcat : varConcat PLUS expression'
    p[0] = p[1] + p[3]

def p_varConcat_plus_expression_after(p):
    'varConcat : expression PLUS varConcat'
    p[0] = p[1] + p[3]
