import webbrowser


showClTree = False
showBrowserTree = False


# command line syntax tree
clTree = []
# syntax tree with brackets style for online tool
browserTree = ''

# functions for command line syntax tree
def cl_tree_append(x, level):
    output = '--- ' * level + str(x)
    global clTree
    clTree.append(output)

def cl_tree_print():
    global clTree
    for x in clTree:
        print(x)

def cl_tree_reset():
    global clTree
    clTree = []

# functions for Online Syntax Tree
def browser_tree_append(x):
    global browserTree
    browserTree = browserTree + x

def browser_open():
    global browserTree
    link = "http://mshang.ca/syntree/?i=" + browserTree
    webbrowser.open_new(link)

def browser_tree_reset():
    global browserTree
    browserTree = ''




# main function called from compiler
def build_tree(tree):
    # reset global variables
    cl_tree_reset()
    browser_tree_reset()

    # start converting syntax tree
    check_tree(tree, 0)

    # outputs
    if showClTree:
        cl_tree_print()
    if showBrowserTree:
        browser_open()




# recursive function to check elements in tree
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
        cl_tree_append('PRINT', level)
        browser_tree_append('[PRINT [(]')
        check(tree[1], level+1)
        browser_tree_append('[)]]')

    # if
    elif tree[0] == 'IF':
        cl_tree_append('IF-STATEMENT', level)
        cl_tree_append('IF', level + 1)
        browser_tree_append('[IF-STATEMENT [IF] [(] ')
        check(tree[1], level + 1)
        browser_tree_append('[)] [{] ')
        check(tree[2], level + 1)
        browser_tree_append('[}] ]')

    # if else
    elif tree[0] == 'IFELSE':
        cl_tree_append('IF-ELSE-STATEMENT', level)
        cl_tree_append('IF', level + 1)
        browser_tree_append('[IF-ELSE-STATEMENT [IF] [(] ')
        check(tree[1], level + 1)
        browser_tree_append('[)] [{] ')
        check(tree[2], level + 1)
        cl_tree_append('ELSE', level + 1)
        browser_tree_append(' [}] [ELSE] [{]')
        check(tree[3], level + 1)
        browser_tree_append('[}] ]')

    # for
    elif tree[0] == 'FOR':
        cl_tree_append('FOR_STATEMENT', level)
        cl_tree_append('FOR', level + 1)
        cl_tree_append(tree[1], level + 1)
        cl_tree_append('IN', level + 1)
        cl_tree_append('NUMBER_OF_ITERATIONS', level + 1)
        browser_tree_append('[FOR-STATEMENT [FOR] '+tree[1]+' [IN] [(] [NUMBER-OF-ITERATIONS')
        check(tree[2], level + 2)
        browser_tree_append('] [)] [{]')
        check(tree[3], level + 1)
        browser_tree_append('[}] ]')

    # for_start_end
    elif tree[0] == 'FOR_START_END':
        cl_tree_append('FOR_STATEMENT', level)
        cl_tree_append('FOR', level + 1)
        cl_tree_append(tree[1], level + 1)
        cl_tree_append('IN', level + 1)
        cl_tree_append('START', level + 1)
        browser_tree_append('[FOR-STATEMENT [FOR] '+tree[1]+' [IN] [(] [START')
        check(tree[2], level + 2)
        cl_tree_append('END', level + 1)
        browser_tree_append('] [;] [END')
        check(tree[3], level + 2)
        browser_tree_append('] [)] [{]')
        check(tree[4], level + 1)
        browser_tree_append('[}] ]')

    # for_start_end_step
    elif tree[0] == 'FOR_START_END_STEP':
        cl_tree_append('FOR_STATEMENT', level)
        cl_tree_append('FOR', level + 1)
        cl_tree_append(tree[1], level + 1)
        cl_tree_append('IN', level + 1)
        cl_tree_append('START', level + 1)
        browser_tree_append('[FOR-STATEMENT [FOR] '+tree[1]+' [IN] [(] [START')
        check(tree[2], level + 2)
        cl_tree_append('END', level + 1)
        browser_tree_append('] [;] [END')
        check(tree[3], level + 2)
        cl_tree_append('STEP', level + 1)
        browser_tree_append('] [;] [STEP')
        check(tree[4], level + 2)
        browser_tree_append('] [)] [{]')
        check(tree[5], level + 1)
        browser_tree_append('[}] ]')

    # while
    elif tree[0] == 'WHILE':
        cl_tree_append('WHILE_STATEMENT', level)
        cl_tree_append('WHILE', level + 1)
        browser_tree_append('[WHILE-STATEMENT [WHILE] [(] ')
        check(tree[1], level + 1)
        browser_tree_append('[)] [{] ')
        check(tree[2], level + 1)
        browser_tree_append('[}] ]')

    # var
    elif tree[0] == 'VAR':
        cl_tree_append('VARIABLE', level)
        cl_tree_append(tree[1], level + 1)
        browser_tree_append('[VAR ['+tree[1]+'] ]')

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
            cl_tree_append('STATEMENTS', level)
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
            cl_tree_append('INTEGER', level)
            browser_tree_append('[INTEGER ' + str(x) + ']')
        elif type(x) is float:
            cl_tree_append('FLOAT', level)
            browser_tree_append('[FLOAT ' + str(x) + ']')
        elif type(x) is bool:
            cl_tree_append('BOOLEAN', level)
            browser_tree_append('[BOOLEAN ' + str(x) + ']')
        elif type(x) is str:
            cl_tree_append('STRING', level)
            browser_tree_append('[STRING ' + str(x) + ']')
        cl_tree_append(x, level + 1)


def calc(tree, level, name, operant):
    browser_tree_append('[')
    cl_tree_append(name + '-STATEMENT', level)
    browser_tree_append(name + '-STATEMENT ')
    check(tree[1], level + 1)
    cl_tree_append('OPERATOR', level + 1)
    cl_tree_append(operant, level + 2)

    if operant == '%':
        operant = '%25'
    if operant == '+':
        operant = 'PLUS'

    browser_tree_append(' [OPERATOR ' + operant + '] ')
    check(tree[2], level + 1)
    browser_tree_append(']')


def cond(tree, level, operant):
    browser_tree_append('[')
    cl_tree_append(tree[0] + '-CONDITION', level)
    browser_tree_append(tree[0] + '-CONDITION ')
    check(tree[1], level + 1)
    cl_tree_append('COMPARISON-OPERATOR', level + 1)
    cl_tree_append(operant, level + 2)
    browser_tree_append(' [COMPARISON-OPERATOR ' + operant + '] ')
    check(tree[2], level + 1)
    browser_tree_append(']')


def assign(tree, level, typ):
    cl_tree_append(typ + 'ASSIGNMENT', level)
    cl_tree_append('NAME', level + 1)
    cl_tree_append(tree[1], level + 2)
    cl_tree_append('VALUE', level + 1)
    if isinstance(tree[2],list):
        browser_tree_append('[' + typ + 'ASSIGNMENT [NAME ' + str(tree[1]) + '] [VALUE')
        check(tree[2], level + 2)
        browser_tree_append(']]')
    else:
        cl_tree_append(tree[2], level + 2)
        browser_tree_append('[' + typ + 'ASSIGNMENT [NAME ' + str(tree[1]) + '] [VALUE ' + str(tree[2]) + ']]')
