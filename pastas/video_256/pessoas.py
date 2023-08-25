from contas import CheckingAccount, SavingAccount


class Person:
    """Person class."""
    def __init__(self, name: str, age: int):
        """Constructor.

        Args:
            name(str): person's name.
            age(int): person's age.
        """
        self.name = name
        self.age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age: int):
        self._age = age

    def __repr__(self):
        """Repr class.

        Returns:
            string with class name and their attributes.
        """
        class_name = type(self).__name__
        attributes = f'({self.name!r}, {self.age!r})'
        return f'{class_name}{attributes}'


class Client(Person):
    """Client class."""
    def __init__(self, name: str, age: int):
        """Constructor.

        Args:
            name(str): client's name.
            age(int): client's age.
        """
        super().__init__(name, age)
        self.account = None


if __name__ == '__main__':
    client_1 = Client('Luiz', 30)
    client_1.account = CheckingAccount(branch=2, account='12341-0', balance=0, protection=10)
    print(client_1)
    print(client_1.account)
    print('##')
    client_2 = Client('Helana', 18)
    client_2.account = SavingAccount(branch=1, account='010215-1', balance=0)
    print(client_2)
    print(client_2.account)
