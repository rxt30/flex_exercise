import ply.yacc as yacc
from lexical import tokens

def p_expression_plus(p):
    'expression : expression PLUS term'
    p[0] = p[1] + p[3]

def p_expression_minus(p):
    'expression : expression MINUS term'
    p[0] = p[1] - p[3]

def p_expression_braces(p):
    'expression : ROUND_START expression ROUND_END'
    p[0] = (p[2])

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_term_multiplication(p):
    'term : term MULTIPLICATION NUMBER'
    p[0] = p[1] * p[3]

def p_term_braces(p):
    'term : ROUND_START term ROUND_END'
    p[0] = (p[2])

def p_term_number(p):
    'term : NUMBER'
    p[0] = p[1]

#Error handling
def p_error(p):
    print("Syntax error in input")

parser = yacc.yacc()
while True:
    result = parser.parse(input("Please enter something:\n"))
    print(result)
