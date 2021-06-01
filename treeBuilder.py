exportTree = ''


def append_tree(x):
    global exportTree
    exportTree = exportTree + x


def print_tree():
    global exportTree
    print(exportTree)


def reset_tree():
    global exportTree
    exportTree = ''


def build_tree(tree):
	reset_tree()
	check_tree(tree, 0)
	print_tree()


def check_tree(tree, level):
    # Calculations
    if tree[0] == 'PLUS':
        calc(tree, level, 'ADDITION', '+')
    elif tree[0] == 'MINUS':
        calc(tree, level, 'SUBTRACTION', '-')
    elif tree[0] == 'MULT':
        calc(tree, level, 'MULTIPLICATION', '*')
    elif tree[0] == 'DIV' or tree[0] == 'INTDIV':
        calc(tree, level, 'DIVISION', '/')
    elif tree[0] == 'MOD':
        calc(tree, level, 'MODULO', '%')

    # Conditions
    elif tree[0] == 'EQUAL':
        cond(tree, level, '==')
    elif tree[0] == 'NOT_EQUAL':
        cond(tree, level, '!=')
    elif tree[0] == 'LEFT_GREATER':
        cond(tree, level, '>')
    elif tree[0] == 'RIGHT_GREATER':
        cond(tree, level, '<')
    elif tree[0] == 'AND':
        cond(tree, level, '&')
    elif tree[0] == 'OR':
        cond(tree, level, '|')

    # print function
    elif tree[0] == 'PRINT':
        myPrint('PRINT', level)
        append_tree('[PRINT ')
        check(tree[1], level)
        append_tree(']')

    # if
    elif tree[0] == 'IF':
        myPrint('IF-STATEMENT', level)
        myPrint('IF', level + 1)
        append_tree('[IF-STATEMENT [IF] [(] ')
        check(tree[1], level + 1)
        append_tree('[)] [{] ')
        check(tree[2], level + 1)
        append_tree('[}] ]')

    # if else
    elif tree[0] == 'IFELSE':
        myPrint('IF-ELSE-STATEMENT', level)
        myPrint('IF', level + 1)
        append_tree('[IF-ELSE-STATEMENT [IF] ')
        check(tree[1], level + 1)
        check(tree[2], level + 1)
        myPrint('ELSE', level + 1)
        append_tree(' [ELSE] ')
        check(tree[3], level + 1)
        append_tree(']')

    # for
    elif tree[0] == 'FOR':
        myPrint('FOR_STATEMENT', level)
        myPrint('FOR', level + 1)
        myPrint('NUMBER_OF_ITERATIONS', level + 1)
        check(tree[1], level + 2)
        check(tree[2], level + 1)

    # for_start_end
    elif tree[0] == 'FOR_START_END':
        myPrint('FOR_STATEMENT', level)
        myPrint('FOR', level + 1)
        myPrint('START', level + 1)
        check(tree[1], level + 2)
        myPrint('END', level + 1)
        check(tree[2], level + 2)
        check(tree[3], level + 1)

    # for_start_end_step
    elif tree[0] == 'FOR_START_END_STEP':
        myPrint('FOR_STATEMENT', level)
        myPrint('FOR', level + 1)
        myPrint('START', level + 1)
        check(tree[1], level + 2)
        myPrint('END', level + 1)
        check(tree[2], level + 2)
        myPrint('STEP', level + 1)
        check(tree[3], level + 2)
        check(tree[4], level + 1)

    # while
    elif tree[0] == 'WHILE':
        myPrint('WHILE_STATEMENT', level)
        myPrint('WHILE', level + 1)
        check(tree[1], level + 1)
        check(tree[2], level + 1)

    # var
    elif tree[0] == 'VAR':
        myPrint('VARIABLE', level)
        myPrint(tree[1], level + 1)
        check(tree[2], level + 2)

    # assignment
    elif tree[0] == 'ASSIGNMENT_INT':
        assign(tree, level, 'INTEGER-')
    elif tree[0] == 'ASSIGNMENT_FLOAT':
        assign(tree, level, 'FLOAT-')
    elif tree[0] == 'ASSIGNMENT_BOOL':
        assign(tree, level, 'BOOLEAN-')
    elif tree[0] == 'ASSIGNMENT_STRING':
        assign(tree, level, 'STRING-')
    elif tree[0] == 'REASSIGNMENT':
        assign(tree, level, 'RE')

    else:
        # check if multiple statements
        if len(tree) > 1:
            myPrint('STATEMENTS', level)
            level += 1
            for x in tree:
                check(x, level)
        else:
            check(tree[0], level)


def check(x, level):
    if isinstance(x, list):
        check_tree(x, level)
    else:
        if type(x) is int:
            myPrint('INTEGER', level)
            append_tree('[INTEGER '+str(x)+']')
        elif type(x) is float:
            myPrint('FLOAT', level)
            append_tree('[FLOAT '+str(x)+']')
        elif type(x) is bool:
            myPrint('BOOLEAN', level)
            append_tree('[BOOLEAN '+str(x)+']')
        elif type(x) is str:
            myPrint('STRING', level)
            append_tree('[STRING '+str(x)+']')
        myPrint(x, level + 1)


def calc(tree, level, name, operant):
    append_tree('[')
    myPrint(name + '-STATEMENT', level)
    append_tree(name + '-STATEMENT ')
    check(tree[1], level + 1)
    myPrint('OPERATOR', level + 1)
    myPrint(operant, level + 2)
    append_tree(' [OPERATOR ' + operant + '] ')
    check(tree[2], level + 1)
    append_tree(']')


def cond(tree, level, operant):
    append_tree('[')
    myPrint(tree[0] + '-CONDITION', level)
    append_tree(tree[0] + '-CONDITION ')
    check(tree[1], level + 1)
    myPrint('COMPARISON-OPERATOR', level + 1)
    myPrint(operant, level + 2)
    append_tree(' [COMPARISON-OPERATOR ' + operant + '] ')
    check(tree[2], level + 1)
    append_tree(']')


def assign(tree, level, typ):
    myPrint(typ + 'ASSIGNMENT', level)
    myPrint('NAME', level + 1)
    myPrint(tree[1], level + 2)
    myPrint('VALUE', level + 1)
    myPrint(tree[2], level + 2)
    append_tree('['+typ+'ASSIGNMENT [NAME '+str(tree[1])+'] [VALUE '+str(tree[2])+']]')


def myPrint(x, level):
    print('--- ' * level + str(x))
