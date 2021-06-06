import ply.yacc as yacc

from error_handling.error import syntax_error
from tokens.tokens import tokens
from syntax.rules.expressions import *
from syntax.rules.terms import *
from syntax.rules.variables import *
from syntax.rules.conditions import *

#Error handling
def p_error(p):
    if p is not None:
        syntax_error(p.lineno)

parser = yacc.yacc(debug=True)
