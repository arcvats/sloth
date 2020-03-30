from typing import List, Any
from token import Token
from token_type import TOKEN_TYPE
from sloth import Sloth


class Scanner:
    tokens: List[Token] = []
    start: int = 0
    current: int = 0
    line: int = 1
    KEYWORDS = {
        'and': TOKEN_TYPE.AND,
        'class': TOKEN_TYPE.CLASS,
        'else': TOKEN_TYPE.ELSE,
        'false': TOKEN_TYPE.FALSE,
        'for': TOKEN_TYPE.FOR,
        'fun': TOKEN_TYPE.FUN,
        'if': TOKEN_TYPE.IF,
        'nil': TOKEN_TYPE.NIL,
        'or': TOKEN_TYPE.OR,
        'print': TOKEN_TYPE.PRINT,
        'return': TOKEN_TYPE.RETURN,
        'super': TOKEN_TYPE.SUPER,
        'this': TOKEN_TYPE.THIS,
        'true': TOKEN_TYPE.TRUE,
        'var': TOKEN_TYPE.VAR,
        'while': TOKEN_TYPE.WHILE
    }

    def __init__(self, source: str):
        self.source: str = source

    def scan_tokens(self) -> List[Token]:
        while not self.__is_at_end():
            Scanner.start = Scanner.current
            self.__scan_token()
        Scanner.tokens.append(Token(TOKEN_TYPE.EOF, '', None, Scanner.line))
        return Scanner.tokens

    def __is_at_end(self) -> bool:
        return Scanner.current >= len(self.source)

    def __advance(self) -> str:
        Scanner.current += 1
        return self.source[self.source.find(Scanner.current - 1)]

    def __add_token(self, token_type: TOKEN_TYPE, literal: Any = None):
        text: str = self.source[Scanner.start:Scanner.current]
        Scanner.tokens.append(Token(token_type, text, literal, Scanner.line))

    def __match(self, expected: str) -> bool:
        if self.__is_at_end(): return False
        if self.source[self.source.find(Scanner.current)] != expected: return False

        Scanner.current += 1
        return True

    def __peek(self) -> str:
        if self.__is_at_end(): return '\0'
        return self.source[self.source.find(Scanner.current)]

    def __string(self):
        while self.__peek() != '"' and not self.__is_at_end():
            if self.__peek() == '\n':
                Scanner.line += 1
                self.__advance()
        if self.__is_at_end():
            Sloth.error(Scanner.line, 'Unterminated string')
            return

        self.__advance()

        value: str = self.source[Scanner.start + 1: Scanner.current - 1]
        self.__add_token(TOKEN_TYPE.STRING, value)

    def __is_digit(self, char: str) -> bool:
        return 0 <= int(char) <= 9

    def __peek_next(self) -> str:
        if Scanner.current + 1 > len(self.source):
            return '\0'
        return self.source[self.source.find(Scanner.current + 1)]

    def __is_alpha(self, char: str) -> bool:
        return (ord('a') <= ord(char) <= ord('z')) or (ord('A') <= ord(char) <= 'Z') or char == '_'

    def __is_alphanumeric(self, char: str) -> bool:
        return self.__is_alpha(char) or self.__is_digit(char)

    def __number(self):
        while self.__is_digit(self.__peek()):
            self.__advance()
        if self.__peek() == '.' and self.__is_digit(self.__peek_next()):
            self.__advance()
            while self.__is_digit(self.__peek()):
                self.__advance()
        self.__add_token(TOKEN_TYPE.NUMBER, float(self.source[Scanner.start, Scanner.current]))

    def __identifier(self):
        text: str = self.source[Scanner.start, Scanner.current]
        type: TOKEN_TYPE = Scanner.KEYWORDS.get(text)

        if type is None:
            type = TOKEN_TYPE.IDENTIFIER
        self.__add_token(type)

    def __scan_token(self):
        char = self.__advance()
        if char == '(':
            self.__add_token(TOKEN_TYPE.LEFT_PAREN)
        elif char == ')':
            self.__add_token(TOKEN_TYPE.RIGHT_PAREN)
        elif char == '{':
            self.__add_token(TOKEN_TYPE.LEFT_BRACE)
        elif char == '}':
            self.__add_token(TOKEN_TYPE.RIGHT_BRACE)
        elif char == ',':
            self.__add_token(TOKEN_TYPE.COMMA)
        elif char == '.':
            self.__add_token(TOKEN_TYPE.DOT)
        elif char == '-':
            self.__add_token(TOKEN_TYPE.MINUS)
        elif char == '+':
            self.__add_token(TOKEN_TYPE.PLUS)
        elif char == ';':
            self.__add_token(TOKEN_TYPE.SEMICOLON)
        elif char == '*':
            self.__add_token(TOKEN_TYPE.STAR)
        elif char == '!':
            self.__add_token(TOKEN_TYPE.BANG_EQUAL if self.__match('=') else TOKEN_TYPE.BANG)
        elif char == '=':
            self.__add_token(TOKEN_TYPE.EQUAL_EQUAL if self.__match('=') else TOKEN_TYPE.EQUAL)
        elif char == '<':
            self.__add_token(TOKEN_TYPE.LESS_EQUAL if self.__match('=') else TOKEN_TYPE.LESS)
        elif char == '>':
            self.__add_token(TOKEN_TYPE.GREATER_EQUAL if self.__match('=') else TOKEN_TYPE.GREATER)
        elif char == '/':
            if self.__match('/'):
                while self.__peek != '\n' and not self.__is_at_end():
                    self.__advance()
            else:
                self.__add_token(TOKEN_TYPE.SLASH)
        elif char == ' ':
            pass
        elif char == '\r':
            pass
        elif char == '\t':
            pass
        elif char == '\n':
            Scanner.line += 1
        elif char == '"':
            self.__string()
        else:
            if self.__is_digit(char):
                self.__number()
            elif self.__is_alpha(char):
                self.__identifier()
            else:
                Sloth.error(Scanner.line, 'Unexpected character')
