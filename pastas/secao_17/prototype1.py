from __future__ import annotations
from typing import List
from copy import deepcopy


class StringReprMixin:
    def __str__(self):
        params = ', '.join(
            [f'{key}={value}' for key, value in self.__dict__.items()]
        )
        return f'{self.__class__.__name__}({params}'

    def __repr__(self):
        return self.__str__()


class Person(StringReprMixin):
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name
        self.addresses: List[Address] = []

    def add_address(self, address: Address):
        self.addresses.append(address)

    def clone(self) -> Person:
        return deepcopy(self)


class Address(StringReprMixin):
    def __init__(self, street: str, number: str):
        self.street = street
        self.number = number


if __name__ == '__main__':
    luiz = Person('Luiz', 'Brasileiro')
    address_luiz = Address('Rua A', '10D')
    luiz.add_address(address_luiz)

    luiz_wife = luiz.clone()
    luiz_wife.first_name = 'Maria Luiza'

    print(luiz)
    print(luiz_wife)
