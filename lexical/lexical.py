import ply.lex as lex
from tokens.tokens import tokens, reserved

t_OR = r'\|\|'
t_AND = r'&&'

t_PLUS = r'\+'
t_ASSIGNMENT = r'='
t_MINUS = r'-'
t_MULTIPLICATION = r'\*'

t_ROUND_START = r'\('
t_ROUND_END = r'\)'
t_CURLY_START = r'\{'
t_CURLY_END = r'\}'

t_QUOTED_CHARS = r'(\"|\').+(\"|\')'
#Ignored Characters
t_ignore = ' \t'
t_ignore_COMMENT = r'\#.*'

#Token with a function
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_CHARS(t):
    r'[A-Za-z]+'
    t.type = reserved.get(t.value,'CHARS')
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


#Error handling
def t_error(t):
    print("Illegal character " + t.value[0] + " on line " + str(t.lexer.lineno))
    t.lexer.skip(1)

lexer = lex.lex()
