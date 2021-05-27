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

    return 'error'
