savedVariables = {}

def p_variable_general(p):
    'variable : CHARS ASSIGNMENT NUMBER'
    print("First Rule")
    savedVariables.update({p[1] : p[3]})
    print(savedVariables)

def p_variable_int(p):
    'variable : "+" CHARS ASSIGNMENT NUMBER'
    savedVariables.update({p[3] : p[5]})
    print(savedVariables)
