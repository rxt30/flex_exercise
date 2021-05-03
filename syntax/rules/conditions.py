# CONDITIONS

def p_condition_true(p):
    'condition : TRUE'
    p[0] = True

def p_condition_false(p):
    'condition : FALSE'
    p[0] = False


def p_condition_equal(p):
    'condition : expression EQUAL expression'
    if p[1] == p[3]:
        p[0] = True
    else:
        p[0] = False

def p_condition_not_equal(p):
    'condition : expression NOT_EQUAL expression'
    if p[1] != p[3]:
        p[0] = True
    else:
        p[0] = False

def p_condition_left_greater(p):
    'condition : expression LEFT_GREATER expression'
    if p[1] > p[3]:
        p[0] = True
    else:
        p[0] = False

def p_condition_right_greater(p):
    'condition : expression RIGHT_GREATER expression'
    if p[1] < p[3]:
        p[0] = True
    else:
        p[0] = False


def p_condition_and(p):
    'condition : condition AND condition'
    if p[1] and p[3]:
        p[0] = True
    else:
        p[0] = False

def p_condition_or(p):
    'condition : condition OR condition'
    if p[1] or p[3]:
        p[0] = True
    else:
        p[0] = False
