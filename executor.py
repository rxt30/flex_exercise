def execute(tree):
    if not isinstance(tree, list):
        return tree

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

    return 'error'
