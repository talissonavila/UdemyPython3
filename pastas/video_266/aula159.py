from dataclasses import dataclass


@dataclass
class Person:
    """Person class."""
    first_name: str
    last_name: str

    @property
    def full_name(self):
        """Returns person's full name."""
        return f'{self.first_name} {self.last_name}.'

    @full_name.setter
    def full_name(self, value):
        first_name, *last_name = value.split()
        self.first_name = first_name
        self.last_name = ' '.join(last_name)


if __name__ == '__main__':
    person_1 = Person('Luiz', 'Miranda')
    print(person_1)
    print(person_1.first_name)
    print(person_1.last_name)
    print(person_1.full_name)
