def p_single_statement(p):
    """statements : statement"""
    p[0] = p[1]

def p_statements(p):
    """statements : statement statements"""
    p[0] = p[1] + p[2]

def p_statement(p):
    """statement  : expression END_OF_STATEMENT
                  | if_statement"""
    p[0] = [p[1]]


def p_expression_plus(p):
    'expression : expression PLUS term'
    p[0] = ['PLUS', p[1], p[3]]

def p_expression_minus(p):
    '''expression : expression MINUS term'''
    p[0] = ['MINUS', p[1], p[3]]

def p_expression_negation(p):
    '''expression : MINUS term'''
    p[0] = ['NEGATION', p[2]]

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




# IF ELSE STATEMENT

def p_if_statement(p):
    'if_statement : IF ROUND_START condition ROUND_END CURLY_START statements CURLY_END'
    if p[3]:
        p[0] = p[6]

def p_if_else_statement(p):
    'if_statement : IF ROUND_START condition ROUND_END CURLY_START statements CURLY_END ELSE CURLY_START statements CURLY_END'
    if p[3]:
        p[0] = p[6]
    else:
        p[0] = p[10]
