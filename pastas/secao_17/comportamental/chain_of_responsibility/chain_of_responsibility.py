def handler_abc(letter: str) -> str:
    letters = ['A', 'B', 'C']

    if letter in letters:
        return f'handler ABC could treate value of {letter}.'
    return handler_def(letter)


def handler_def(letter: str) -> str:
    letters = ['D', 'E', 'F']

    if letter in letters:
        return f'handler DEF could treate value of {letter}.'
    return handler_unsolved(letter)


def handler_unsolved(letter: str) -> str:
    return f'handler unsolved can not treate value of {letter}.'


if __name__ == '__main__':
    print(handler_abc('A'))
    print(handler_abc('F'))
    print(handler_abc('G'))
