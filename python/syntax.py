import sys
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
    'term : term MULTIPLICATION term'
    p[0] = p[1] * p[3]

def p_term_expression(p):
    'term : ROUND_START expression ROUND_END MULTIPLICATION term'
    p[0] = (p[2]) * p[5]

def p_term_expression_single(p):
    'term : ROUND_START expression ROUND_END'
    p[0] = (p[2])

def p_term_number(p):
    'term : NUMBER'
    p[0] = p[1]

def p_term_chars(p):
    'term : CHARS'
    p[0] = p[1]

#Error handling
def p_error(p):
    print("Syntax error")

parser = yacc.yacc()
if len(sys.argv) == 1:
    while True:
        result = parser.parse(input("Please enter something:\n"))
        print(result)
else:
    f = open(sys.argv[1])
    content = f.readlines()
    for line in content:
        parsed_line = parser.parse(line)
        print(parsed_line)
