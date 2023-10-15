from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Colleague(ABC):
    def __init__(self):
        self.name: str = ''

    @abstractmethod
    def broadcast(self, message: str):
        pass

    @abstractmethod
    def direct(self, message: str):
        pass


class Person(Colleague):
    def __init__(self, name: str, mediator: Mediator):
        super().__init__()
        self.name = name
        self.mediator = mediator

    def broadcast(self, message: str):
        self.mediator.broadcast(self, message)

    def send_direct(self, receiver: str, message: str):
        self.mediator.direct(self, receiver, message)

    def direct(self, message: str):
        print(message)


class Mediator(ABC):
    @abstractmethod
    def broadcast(self, colleague: Colleague, message: str):
        pass

    @abstractmethod
    def direct(self, sender: Colleague, receiver: str, message: str):
        pass


class Chatroom(Mediator):
    def __init__(self):
        self.coleagues: List[Colleague] = []

    def is_colleague(self, colleague: Colleague) -> bool:
        return colleague in self.coleagues

    def add_colleague(self, colleague: Colleague):
        if not self.is_colleague(colleague):
            self.coleagues.append(colleague)

    def remove_colleague(self, colleague: Colleague):
        if self.is_colleague(colleague):
            self.coleagues.remove(colleague)

    def broadcast(self, colleague: Colleague, message: str):
        if not self.is_colleague(colleague):
            return
        print(f'{colleague.name} said: {message}')

    def direct(self, sender: Colleague, receiver: str, message: str):
        if not self.is_colleague(sender):
            return

        receiver_object: List[Colleague] = [
            colleague for colleague in self.coleagues
            if colleague.name == receiver
        ]

        if not receiver_object:
            return
        receiver_object[0].direct(
            f'{sender.name} to {receiver_object[0].name}: {message}'
        )


if __name__ == '__main__':
    chat = Chatroom()
    joao = Person('Joao', chat)
    elis = Person('Elis', chat)
    jose = Person('Jose', chat)
    maria = Person('Maria', chat)

    chat.add_colleague(joao)
    chat.add_colleague(maria)
    chat.add_colleague(elis)

    joao.broadcast('Hey everyone!')
    maria.broadcast('Hey joao.')

    jose.broadcast('Chat me plx')

    joao.send_direct('Elis', 'Hey elis. nice 2 meet u')
    elis.send_direct('Joao', 'no')
