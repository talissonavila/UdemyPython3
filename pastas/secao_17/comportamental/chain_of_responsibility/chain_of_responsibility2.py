from abc import ABC, abstractmethod


class Handler(ABC):
    def __init__(self):
        self.sucessor: Handler

    @abstractmethod
    def handle(self, letter: str) -> str:
        pass


class HandlerABC(Handler):
    def __init__(self, sucessor: Handler):
        super().__init__()
        self.letters = ['A', 'B', 'C']
        self.sucessor = sucessor

    def handle(self, letter: str) -> str:
        if letter in self.letters:
            return f'{self.__class__.__name__} can treate {letter}.'
        return self.sucessor.handle(letter)


class HandlerDEF(Handler):
    def __init__(self, sucessor: Handler):
        super().__init__()
        self.letters = ['D', 'E', 'F']
        self.sucessor = sucessor

    def handle(self, letter: str) -> str:
        if letter in self.letters:
            return f'{self.__class__.__name__} can trate {letter}.'
        return self.sucessor.handle(letter)


class HandlerUnsolved(Handler):
    def handle(self, letter: str) -> str:
        return f'No one can treate {letter}.'


if __name__ == '__main__':
    handler_unsolved = HandlerUnsolved()
    handler_def = HandlerDEF(handler_unsolved)
    handler_abc = HandlerABC(handler_def)

    print(handler_abc.handle('A'))
    print(handler_abc.handle('B'))
    print(handler_abc.handle('C'))

    print(handler_abc.handle('D'))
    print(handler_abc.handle('F'))
    print(handler_unsolved.handle('H'))
    print(handler_unsolved.handle('A'))
    print(handler_def.handle('A'))
