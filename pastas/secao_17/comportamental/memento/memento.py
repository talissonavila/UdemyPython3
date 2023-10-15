from __future__ import annotations
from typing import Dict, List
from copy import deepcopy


class Memento:
    def __init__(self, state: Dict):
        self._state: Dict
        super().__setattr__('_state', state)

    def get_state(self) -> Dict:
        return self._state

    def __setattr__(self, name, value):
        raise AttributeError('Sorry. I am immutable.')


class ImageEditor:
    def __init__(self, file_name: str, width: int, height: int):
        self.file_name = file_name
        self.width = width
        self.height = height

    def save_state(self) -> Memento:
        return Memento(deepcopy(self.__dict__))

    def restore(self, memento: Memento):
        self.__dict__ = memento.get_state()

    def __str__(self):
        return f'{self.__class__.__name__}({self.__dict__}'


class Caretaker:
    def __init__(self, originator: ImageEditor):
        self._originator = originator
        self._mementos: List[Memento] = []

    def backup(self):
        self._mementos.append(self._originator.save_state())

    def restore(self):
        if not self._mementos:
            return

        self._originator.restore(self._mementos.pop())


if __name__ == '__main__':
    image = ImageEditor('picture1.jpg', 111, 111)
    caretaker = Caretaker(image)
    caretaker.backup()

    image.file_name = 'picture1_changed.png'
    image.width = 222
    image.height = 222
    caretaker.backup()

    image.file_name = 'picture1_changed2.png'
    image.width = 333
    image.height = 333
    caretaker.backup()

    image.file_name = 'picture1_changed3.png'
    image.width = 444
    image.height = 444

    caretaker.restore()
    caretaker.restore()
    caretaker.restore()
    caretaker.restore()
    caretaker.restore()
    caretaker.restore()
    caretaker.restore()

    print(image)
