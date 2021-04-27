import ply.lex as lex
from tokens import tokens

t_INTEGER = r'int'
t_STRING = r'string'
t_BOOLEAN = r'bool'

t_IF = r'if'
t_FOR = r'for'
t_WHILE = r'while'
t_TRUE = r'true'
t_FALSE = r'false'
t_OR = r'\|\|'
t_AND = r'&&'

t_PLUS = r'\+'
t_ASSIGNMENT = r'='
t_MINUS = r'-'
t_MULTIPLICATION = r'\*'
t_CHARS = r'[A-Za-z]+'

t_ROUND_START = r'\('
t_ROUND_END = r'\)'
t_CURLY_START = r'\{'
t_CURLY_END = r'\}'

#Ignored Characters
t_ignore = ' \t'

#Token with a function
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

#Error handling
def t_error(t):
    print("Illegal character " + t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()
