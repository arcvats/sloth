from sys import exit
from os import path
from scanner import Scanner
from token import Token

from typing import List, TextIO


class Sloth:
    had_error: bool = False

    @staticmethod
    def main(*args: List[str]):
        if len(args) > 1:
            print('Usage: sloth [script]')
            exit(64)
        elif len(args) == 1:
            Sloth.__run_file(args[0])
        else:
            Sloth.__run_prompt()

    @staticmethod
    def __run_file(rel_path: str):
        handler: TextIO = open(path.relpath(rel_path), 'r')
        file_str: str = handler.read()
        handler.close()
        Sloth.__run(file_str)
        if Sloth.had_error:
            exit(65)

    @staticmethod
    def __run_prompt():
        input_str: str = str(input())
        while True:
            print('> ', end='')
            Sloth.__run(input_str)
            Sloth.had_error = False

    @staticmethod
    def __run(source: str):
        scanner: Scanner = Scanner(source)
        tokens: List[Token] = scanner.scan_tokens()

        for token in tokens:
            print(token)

    @staticmethod
    def error(line: int, message: str):
        Sloth.__report(line, '', message)

    @staticmethod
    def __report(line: int, where: str, message: str):
        print('[line %s ] Error %s : %s' % line % where % message)
        Sloth.had_error = True


if __name__ == '__main__':
    Sloth.main()