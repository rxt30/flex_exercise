reserved = {
    'int' : 'INTEGER',
    'float' : 'FLOAT',
    'string' : 'STRING',
    'bool' : 'BOOLEAN',
    'if' : 'IF',
    'else' : 'ELSE',
    'for' : 'FOR',
    'while' : 'WHILE',
    'true' : 'TRUE',
    'false' : 'FALSE',
    '==' : 'EQUAL',
    '!=' : 'NOT_EQUAL'
}

tokens = [
    'SEMICOLON',
    'OR',
    'AND',
    'ASSIGNMENT',
    'PLUS',
    'MULTIPLICATION',
    'MINUS',
    'DIVISION',
    'MODULO',
    'INVERSE',
    'RIGHT_GREATER',
    'LEFT_GREATER',
    'CHARS',
    'QUOTED_CHARS',
    'NUMBER',
    'ROUND_START',
    'ROUND_END',
    'CURLY_START',
    'CURLY_END',
    'COMMENT'
] + list(reserved.values())
