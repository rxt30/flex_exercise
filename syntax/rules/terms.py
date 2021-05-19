def p_term_multiplication(p):
    'term : term MULTIPLICATION term'
    p[0] = p[1] * p[3]

def p_term_diviosion(p):
    'term : term DIVISION term'
    if p[3] != 0:
        p[0] = p[1] / p[3]
    else:
        print("The denominator can not be zero")
        #print("Syntax error on line " +str(line)+ "\n")
        raise SyntaxError

def p_term_diviosion_with_no_remainder(p):
    'term : term DIVISION DIVISION term'
    if p[3] != 0:
        p[0] = p[1] // p[4]
    else:
        print("The denominator can not be zero")
        #print("Syntax error on line " +str(line)+ "\n")
        raise SyntaxError

def p_term_modulo(p):
    'term : term MODULO term'
    if p[3] != 0:
        p[0] = p[1] % p[3]
    else:
        print("The denominator can not be zero")
        #äprint("Syntax error on line " +str(line)+ "\n")
        raise SyntaxError

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
