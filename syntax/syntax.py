import ply.yacc as yacc
from tokens.tokens import tokens
from syntax.rules.expressions import *
from syntax.rules.terms import *
from syntax.rules.variables import *
from syntax.rules.conditions import *
from syntax.rules.varConcat import *

#Error handling
def p_error(p):
    if p is not None:
        print("Syntax error on line " + str(p.lineno) + " at position " + str(p.lexpos) + "\n")

parser = yacc.yacc(debug=True)
