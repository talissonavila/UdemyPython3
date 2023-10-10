from abc import ABC, abstractmethod


class StringReprMixin:
    def __str__(self):
        params = ', '.join(
            [f'{key}={value}' for key, value in self.__dict__.items()]
        )
        return f'{self.__class__.__name__}({params}'

    def __repr__(self):
        return self.__str__()


class User(StringReprMixin):
    def __init__(self):
        self.first_name = None
        self.last_name = None
        self.age = None
        self.phone_numbers = []
        self.addresses = []


class IUserBuilder(ABC):
    @property
    @abstractmethod
    def result(self): pass

    @abstractmethod
    def add_first_name(self, first_name): pass

    @abstractmethod
    def add_last_name(self, last_name): pass

    @abstractmethod
    def add_age(self, age): pass

    @abstractmethod
    def add_phone(self, phone): pass

    @abstractmethod
    def add_adress(self, address): pass


class UserBuilder(IUserBuilder):
    def __init__(self):
        self.reset()

    def reset(self):
        self._result = User()

    @property
    def result(self):
        return_data = self._result
        self.reset()
        return return_data

    def add_first_name(self, first_name):
        self._result.first_name = first_name

    def add_last_name(self, last_name):
        self._result.last_name = last_name

    def add_age(self, age):
        self._result.age = age

    def add_phone(self, phone):
        self._result.phone_numbers.append(phone)

    def add_adress(self, adress):
        self._result.addresses.append(adress)


class UserDirector:
    def __init__(self, builder: UserBuilder):
        self._builder = builder

    def with_age(self, first_name, last_name, age):
        self._builder.add_first_name(first_name)
        self._builder.add_last_name(last_name)
        self._builder.add_age(age)
        return self._builder.result

    def with_address(self, first_name, last_name, address):
        self._builder.add_first_name(first_name)
        self._builder.add_last_name(last_name)
        self._builder.add_adress(address)
        return self._builder.result


if __name__ == '__main__':
    user_builder = UserBuilder()
    user_director = UserDirector(user_builder)

    user1 = user_director.with_age('Lucas', 'Moura', 29)
    print(user1)

    user2 = user_director.with_address('Wellington', 'Rato', 'CT Barra Funda')
    print(user2)
    