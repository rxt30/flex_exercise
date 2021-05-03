reserved = {
    'int' : 'INTEGER',
    'string' : 'STRING',
    'bool' : 'BOOLEAN',
    'if' : 'IF',
    'else' : 'ELSE',
    'for' : 'FOR',
    'while' : 'WHILE',
    'true' : 'true',
    'false' : 'false'
}

tokens = [
    'OR',
    'AND',
    'ASSIGNMENT',
    'PLUS',
    'MULTIPLICATION',
    'MINUS',
    'INVERSE',
    'RIGHT_GREATER',
    'LEFT_GREATER',
    'CHARS',
    'NUMBER',
    'ROUND_START',
    'ROUND_END',
    'CURLY_START',
    'CURLY_END',
    'COMMENT'
] + list(reserved.values())
