from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class BoxStructure(ABC):
    @abstractmethod
    def print_content(self):
        pass

    @abstractmethod
    def get_price(self) -> float:
        pass

    def add(self, child: BoxStructure):
        pass

    def remove(self, child: BoxStructure):
        pass


class Box(BoxStructure):
    def __init__(self, box_name: str):
        self.box_name = box_name
        self._children: List[BoxStructure] = []

    def print_content(self):
        print(f'\n{self.box_name}:')
        for child in self._children:
            child.print_content()

    def get_price(self) -> float:
        return sum([
                child.get_price() for child in self._children
            ])

    def add(self, child: BoxStructure):
        self._children.append(child)

    def remove(self, child: BoxStructure):
        if child in self._children:
            self._children.remove(child)


class Product(BoxStructure):
    def __init__(self, product_name: str, price: float):
        self.product_name = product_name
        self.price = price

    def print_content(self):
        print(self.product_name, self.price)

    def get_price(self) -> float:
        return self.price


if __name__ == '__main__':
    t_shirt1 = Product('T-shirt 1 ', 49.90)
    t_shirt2 = Product('T-shirt 2 ', 29.90)
    t_shirt3 = Product('T-shirt 3 ', 99.90)
    t_shirt3.print_content()

    t_shirt_box = Box('T-shirt box')
    t_shirt_box.add(t_shirt1)
    t_shirt_box.add(t_shirt2)
    t_shirt_box.add(t_shirt3)

    t_shirt_box.print_content()

    smartphone1 = Product('Smartphone 1 ', 1450)
    smartphone2 = Product('Smartphone 2 ', 14500)

    smartphone_box = Box('Smartphone box')
    smartphone_box.add(smartphone1)
    smartphone_box.add(smartphone2)

    smartphone_box.print_content()

    print('--'* 10)
    big_box = Box('Big box')
    big_box.add(t_shirt_box)
    big_box.add(smartphone_box)
    big_box.print_content()
    print(big_box.get_price())
