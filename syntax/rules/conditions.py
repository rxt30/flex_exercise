# CONDITIONS

def p_condition_true(p):
    'condition : TRUE'
    p[0] = True

def p_condition_false(p):
    'condition : FALSE'
    p[0] = False

def p_condition_expression(p):
    'condition : CHARS'
    p[0] = ['VAR', p[1], p.lineno(1)]

def p_condition_equal(p):
    'condition : expression EQUAL expression'
    p[0] = ['EQUAL', p[1], p[3]]

def p_condition_not_equal(p):
    'condition : expression NOT_EQUAL expression'
    p[0] = ['NOT_EQUAL', p[1], p[3]]

def p_condition_left_greater(p):
    'condition : expression LEFT_GREATER expression'
    p[0] = ['LEFT_GREATER', p[1], p[3]]

def p_condition_right_greater(p):
    'condition : expression RIGHT_GREATER expression'
    p[0] = ['RIGHT_GREATER', p[1], p[3]]

def p_condition_and(p):
    'condition : expression AND expression'
    p[0] = ['AND', p[1], p[3]]

def p_condition_or(p):
    'condition : expression OR expression'
    p[0] = ['OR', p[1], p[3]]
