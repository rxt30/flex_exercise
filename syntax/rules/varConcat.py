from syntax.rules.savedVariables import *

def p_varConcat_plus(p):
    "varConcat : CHARS PLUS varConcat"
    p[0] = getVariable(p[1], p.lineno(1)) + p[3]

def p_varConcat_chars(p):
    "varConcat : CHARS"
    p[0] = getVariable(p[1], p.lineno(1))
