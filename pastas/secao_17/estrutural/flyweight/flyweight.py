from __future__ import annotations
from typing import Dict, List


class Client:
    def __init__(self, name: str):
        self.name = name
        self._addresses: List = []

        self.address_number: str = ''
        self.address_details: str = ''

    def add_address(self, address: Address):
        self._addresses.append(address)

    def list_addresses(self):
        for address in self._addresses:
            address.show_address(self.address_number, self.address_details)


class Address:
    def __init__(self, street: str, neighbourhood: str, zip_code: str):
        self._street = street
        self._neighbourhood = neighbourhood
        self._zip_code = zip_code

    def show_address(self, address_number: str, address_details: str):
        print(
            self._street, address_number, self._neighbourhood, address_details, self._zip_code
        )


class AddressFactory:
    _addresses: Dict = {}

    def _get_key(self, **kwargs):
        return ''.join(kwargs.values())

    def get_address(self, **kwargs) -> str:
        key = self._get_key(**kwargs)

        try:
            address_flyweight = self._addresses[key]
            print('using object already created')
        except KeyError:
            address_flyweight = Address(**kwargs)
            self._addresses[key] = address_flyweight
            print('creating new object')

        return address_flyweight


if __name__ == '__main__':
    address_factory = AddressFactory()

    address1 = address_factory.get_address(street='Rua A', neighbourhood='Centro', zip_code='000123-040')
    address2 = address_factory.get_address(street='Rua A', neighbourhood='Centro', zip_code='000123-040')

    luiz = Client('Luiz')
    luiz.address_number = '50'
    luiz.address_details = 'C'
    luiz.add_address(address1)
    luiz.list_addresses()

    maria = Client('Maria')
    maria.address_number = '1050'
    maria.address_details = 'Apto 55C'
    maria.add_address(address1)
    maria.list_addresses()
