from token_type import TOKEN_TYPE
from typing import Any


class Token:
    def __init__(self, token_type: TOKEN_TYPE, lexeme: str, literal: Any, line: int):
        self.type: TOKEN_TYPE = token_type
        self.lexeme: str = lexeme
        self.literal: Any = literal
        self.line: int = line

    def __str__(self) -> str:
        return self.type + " " + self.lexeme + " " + self.literal
