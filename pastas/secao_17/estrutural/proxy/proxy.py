from __future__ import annotations
from abc import ABC, abstractmethod
from time import sleep
from typing import Dict, List


class IUser(ABC):
    first_name: str
    last_name: str

    @abstractmethod
    def get_addresses(self) -> List[Dict]:
        pass

    @abstractmethod
    def get_all_user_data(self) -> Dict:
        pass


class RealUser(IUser):
    def __init__(self, first_name: str, last_name: str):
        sleep(2)
        self.first_name = first_name
        self.last_name = last_name

    def get_addresses(self) -> List[Dict]:
        sleep(2)
        return [
            {'rua': 'Av. Brasil', 'numero': '500'}
        ]

    def get_all_user_data(self) -> Dict:
        sleep(2)
        return {
            'cpf': '123.465.789-00',
            'rg': '1204678357-7'
        }


class UserProxy(IUser):
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

        self._real_user: RealUser
        self._cached_addresses: List[Dict]
        self._all_user_data: Dict

    def get_real_user(self):
        if not hasattr(self, '_real_user'):
            self._real_user = RealUser(self.first_name, self.last_name)

    def get_addresses(self) -> List[Dict]:
        self.get_real_user()

        if not hasattr(self, '_cached_addresses'):
            self._cached_addresses = self._real_user.get_addresses()
        return self._cached_addresses

    def get_all_user_data(self) -> Dict:
        self.get_real_user()

        if not hasattr(self, '_all_user_data'):
            self._all_user_data = self._real_user.get_all_user_data()
        return self._all_user_data


if __name__ == '__main__':
    luiz = UserProxy('Luiz', 'Miranda')
    print(luiz.first_name)
    print(luiz.last_name)

    print(luiz.get_all_user_data())
    print(luiz.get_addresses())

    print('cached data\n')
    for i in range(50):
        print(luiz.get_addresses())
