from error_handling.error import wrong_assignment_error, wrong_reassignment_error, denominator_error
from syntax.rules.savedVariables import savedVariables, getVariable


def execute_tree(syntax_tree):
    if syntax_tree:
        for statement in syntax_tree:
            result = execute(statement)
            if result is not None:
                print(result)


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
        if execute(tree[2]) != 0:
            return execute(tree[1]) / execute(tree[2])
        else:
            denominator_error(tree[3])

    if tree[0] == 'INTDIV':
        if execute(tree[2]) != 0:
            return execute(tree[1]) // execute(tree[2])
        else:
            denominator_error(tree[3])

    if tree[0] == 'MOD':
        if execute(tree[2]) != 0:
            return execute(tree[1]) % execute(tree[2])
        else:
            denominator_error(tree[3])

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

    # print function
    # TODO: print AND/OR return value?
    if tree[0] == 'PRINT':
        print(execute(tree[1]))
        return

    # if statements
    if tree[0] == 'IF':
        print('IF-START')
        if execute(tree[1]):
            execute_tree(tree[2])
        return 'IF-END'

    if tree[0] == 'IFELSE':
        print('IFELSE-START')
        if execute(tree[1]):
            execute_tree(tree[2])
        else:
            execute_tree(tree[3])
        return 'IFELSE-END'

    # loops
    if tree[0] == 'FOR':
        loop_repetitions = int(execute(tree[1]))
        print('FOR-LOOP-START (' + str(loop_repetitions) + ')')
        for x in range(loop_repetitions):
            execute_tree(tree[2])
        return 'FOR-LOOP-END'

    # TODO: Wollen wir tatsächlich FOR-Loops ohne Laufvariable?
    if tree[0] == 'FOR_START_END':
        print('FOR-START-END-LOOP-START')
        for x in range(int(execute(tree[1])), int(execute(tree[2]))):
            execute_tree(tree[3])
        return 'FOR-START-END-LOOP-END'

    if tree[0] == 'FOR_START_END_STEP':
        print('FOR-START-END-STEP-LOOP-START')
        for x in range(int(execute(tree[1])), int(execute(tree[2])), int(execute(tree[3]))):
            execute_tree(tree[4])
        return 'FOR-START-END-STEP-LOOP-END'

    if tree[0] == 'WHILE':
        print('WHILE-LOOP-START')
        while execute(tree[1]):
            execute_tree(tree[2])
        return 'WHILE-LOOP-END'

    # ---VARIABLES---
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
        savedVariables.update({tree[1]: execute(tree[2])})
        print(savedVariables)
        return 'ASSIGNMENT_BOOL-END'

    # reassignment
    if tree[0] == 'REASSIGNMENT':
        savedVariableType = type(savedVariables[tree[1]])
        if not (tree[1] in savedVariables and isinstance(execute(tree[2]), savedVariableType)):
            if not (isinstance(execute(tree[2]), (float, int)) and isinstance(savedVariables[tree[1]], (float, int))):
                wrong_reassignment_error(tree[3])

        if savedVariableType is str:
            savedVariables.update({tree[1]: execute(tree[2]).strip("'\"")})
        elif savedVariableType is int:
            savedVariables.update({tree[1]: int(execute(tree[2]))})
        elif savedVariableType is float:
            savedVariables.update({tree[1]: float(execute(tree[2]))})
        elif savedVariableType is bool:
            savedVariables.update({tree[1]: execute(tree[2])})

        print(savedVariables)
        return 'REASSIGNMENT-END'

    return 'NO_EXECUTION_RULE_ERROR'
