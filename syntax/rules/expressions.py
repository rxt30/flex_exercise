def p_single_statement(p):
    """statements : statement"""
    p[0] = p[1]

def p_statements(p):
    """statements : statement statements"""
    p[0] = p[1] + p[2]

def p_statement(p):
    """statement  : expression SEMICOLON
                  | if_statement
                  | loop
                  | variable SEMICOLON
                  | empty"""
    p[0] = [p[1]]

def p_empty(p):
    'empty :'

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

def p_expression_condition(p):
    'expression : condition'
    p[0] = p[1]


# PRINT FUNCTION

def p_print(p):
    'expression : PRINT ROUND_START expression ROUND_END'
    p[0] = ['PRINT', p[3]]


# IF ELSE STATEMENT

def p_if_statement(p):
    'if_statement : IF ROUND_START condition ROUND_END CURLY_START statements CURLY_END'
    p[0] = ['IF', p[3], p[6]]

def p_if_else_statement(p):
    'if_statement : IF ROUND_START condition ROUND_END CURLY_START statements CURLY_END ELSE CURLY_START statements CURLY_END'
    p[0] = ['IFELSE', p[3], p[6], p[10]]

# FOR LOOP
def p_for_loop(p):
    'loop : FOR CHARS IN ROUND_START NUMBER ROUND_END CURLY_START statements CURLY_END'
    p[0] = ['FOR', p[2], p[5], p[8], p.lineno(1)]

def p_for_loop_start_end(p):
    'loop : FOR CHARS IN ROUND_START NUMBER SEMICOLON NUMBER ROUND_END CURLY_START statements CURLY_END'
    p[0] = ['FOR_START_END', p[2], p[5], p[7], p[10], p.lineno(1)]

def p_for_loop_start_end_step(p):
    'loop : FOR CHARS IN ROUND_START NUMBER SEMICOLON NUMBER SEMICOLON NUMBER ROUND_END CURLY_START statements CURLY_END'
    p[0] = ['FOR_START_END_STEP', p[2], p[5], p[7], p[9], p[12], p.lineno(1)]


# WHILE LOOP

def p_while_loop(p):
    'loop : WHILE ROUND_START condition ROUND_END CURLY_START statements CURLY_END'
    p[0] = ['WHILE', p[3], p[6]]
