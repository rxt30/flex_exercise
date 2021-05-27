from error_handling.error import wrong_assignment_error, wrong_reassignment_error
from syntax.rules.savedVariables import savedVariables, getVariable


def execute(tree):
    # Termination condition for recursion
    if not isinstance(tree, list):
        return tree

    # basic arithmetic
    if tree[0] == 'PLUS':
        return execute(tree[1]) + execute(tree[2])

    if tree[0] == 'MINUS':
        return execute(tree[1]) - execute(tree[2])

    if tree[0] == 'NEGATION':
        return -execute(tree[1])

    if tree[0] == 'MULT':
        return execute(tree[1]) * execute(tree[2])

    if tree[0] == 'DIV':
        return execute(tree[1]) / execute(tree[2])

    if tree[0] == 'INTDIV':
        return execute(tree[1]) // execute(tree[2])

    if tree[0] == 'MOD':
        return execute(tree[1]) % execute(tree[2])

    # conditions
    if tree[0] == 'EQUAL':
        return execute(tree[1]) == execute(tree[2])

    if tree[0] == 'NOT_EQUAL':
        return execute(tree[1]) != execute(tree[2])

    if tree[0] == 'LEFT_GREATER':
        return execute(tree[1]) > execute(tree[2])

    if tree[0] == 'RIGHT_GREATER':
        return execute(tree[1]) < execute(tree[2])

    if tree[0] == 'AND':
        return execute(tree[1]) & execute(tree[2])

    if tree[0] == 'OR':
        return execute(tree[1]) | execute(tree[2])


    # if statements
    if tree[0] == 'IF':
        print('IF-START')
        if tree[1]:
            for statement in tree[2]:
                executed_statement = str(execute(statement))
                print('   ' + executed_statement)
        return 'IF-END'

    if tree[0] == 'IFELSE':
        print('IFELSE-START')
        if tree[1]:
            for statement in tree[2]:
                executed_statement = str(execute(statement))
                print('   ' + executed_statement)
        else:
            for statement in tree[3]:
                executed_statement = str(execute(statement))
                print('   ' + executed_statement)
        return 'IFELSE-END'

    # for loops
    if tree[0] == 'FOR':
        loop_repetitions = int(tree[1])
        print('LOOP-START (' + str(loop_repetitions) + ')')
        for x in range(loop_repetitions):
            for statement in tree[2]:
                executed_statement = str(execute(statement))
                print('   ' + executed_statement)
        return 'LOOP-END'


    ### variables

    # resolve variable
    if tree[0] == "VAR":
        return getVariable(tree[1], tree[2])

    # integer assignment
    if tree[0] == 'ASSIGNMENT_INT':
        if not isinstance(execute(tree[2]), (float, int)):
            wrong_assignment_error(tree[3])
        savedVariables.update({tree[1]: int(execute(tree[2]))})
        print(savedVariables)
        return 'ASSIGNMENT_INT-END'

    # float assignment
    if tree[0] == 'ASSIGNMENT_FLOAT':
        if not isinstance(execute(tree[2]), (float, int)):
            wrong_assignment_error(tree[3])
        savedVariables.update({tree[1]: float(execute(tree[2]))})
        print(savedVariables)
        return 'ASSIGNMENT_FLOAT-END'

    # string assignment
    if tree[0] == 'ASSIGNMENT_STRING':
        if type(execute(tree[2])) is not str:
            wrong_assignment_error(tree[3])
        savedVariables.update({tree[1]: execute(tree[2]).strip("'\"")})
        print(savedVariables)
        return 'ASSIGNMENT_STRING-END'

    # boolean assignment
    if tree[0] == 'ASSIGNMENT_BOOL':
        if type(execute(tree[2])) is not bool:
            wrong_assignment_error(tree[3])
        savedVariables.update({execute(tree[1]): execute(tree[2])})
        print(savedVariables)
        return 'ASSIGNMENT_BOOL-END'

    # reassignment
    if tree[0] == 'REASSIGNMENT':
        if not (tree[1] in savedVariables and type(execute(tree[2])) == type(savedVariables[tree[1]])):
            if not(isinstance(execute(tree[3]), (float, int)) and isinstance(savedVariables[tree[1]], (float, int))):
                wrong_reassignment_error(tree[3])

        savedVariableType = type(savedVariables[tree[1]])
        if savedVariableType is str:
            savedVariables.update({tree[1]: execute(tree[2]).strip("'\"")})
        elif savedVariableType is int:
            savedVariables.update({tree[1]: int(execute(tree[2]))})
        elif savedVariableType is float:
            savedVariables.update({tree[1]: float(execute(tree[2]))})
        elif savedVariableType is bool:
            savedVariables.update({tree[1]: execute(tree[2]) == True})

        print(savedVariables)
        return 'REASSIGNMENT-END'

    return 'error'
