from collections.abc import Iterator, Iterable
from typing import Any, List


class MyIterator(Iterator):
    def __init__(self, collection: List[Any]):
        self._collection = collection
        self._index = 0

    def __next__(self):
        try:
            item = self._collection[self._index]
            self._index += 1
            return item
        except IndexError:
            raise StopIteration


class ReverseIterator(Iterator):
    def __init__(self, collection: List[Any]):
        self._collection = collection
        self._index = -1

    def __next__(self):
        try:
            item = self._collection[self._index]
            self._index -= 1
            return item
        except IndexError:
            raise StopIteration


class MyList(Iterable):
    def __init__(self):
        self._items: List[Any] = []
        self._my_iterator = MyIterator(self._items)

    def add(self, value: Any):
        self._items.append(value)

    def __iter__(self) -> Iterator:
        return self._my_iterator

    def reverse_iterator(self) -> Iterator:
        return ReverseIterator(self._items)

    def __str__(self) -> str:
        return f'{self.__class__.__name__}({self._items})'


if __name__ == '__main__':
    mylist = MyList()
    mylist.add('Eu')
    mylist.add('Tu')
    mylist.add('Ele')

    # print(mylist)
    print('roubei:', next(iter(mylist)))

    for _value in mylist:
        print(_value)
    print()
    for _value in mylist.reverse_iterator():
        print(_value)
