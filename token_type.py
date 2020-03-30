from enum import Enum
from typing import List

SINGLE_CHAR_TOKENS: List[str] = [
    'LEFT_PAREN', 'RIGHT_PAREN', 'LEFT_BRACE', 'RIGHT_BRACE',
    'COMMA', 'DOT', 'MINUS', 'PLUS', 'SEMICOLON', 'SLASH', 'STAR',
]

ONE_OR_TWO_CHAR_TOKENS: List[str] = [
    'BANG', 'BANG_EQUAL',
    'EQUAL', 'EQUAL_EQUAL',
    'GREATER', 'GREATER_EQUAL',
    'LESS', 'LESS_EQUAL',
]

LITERALS: List[str] = ['IDENTIFIER', 'STRING', 'NUMBER']

KEYWORDS: List[str] = [
    'AND', 'CLASS', 'ELSE', 'FALSE', 'FUN', 'FOR', 'IF', 'NIL', 'OR',
    'PRINT', 'RETURN', 'SUPER', 'THIS', 'TRUE', 'VAR', 'WHILE',
    'EOF'
]

ALL_TOKENS: List[str] = SINGLE_CHAR_TOKENS + ONE_OR_TWO_CHAR_TOKENS + LITERALS + KEYWORDS

TOKEN_TYPE: Enum = Enum('TokenType', ALL_TOKENS)
