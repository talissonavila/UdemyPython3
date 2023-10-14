from abc import ABC, abstractmethod


class Pizza(ABC):
    def prepare(self):
        self.hook_before_add_ingredients()
        self.add_ingredients()
        self.hook_after_add_ingredients()
        self.cook()
        self.cut()
        self.serve()

    def hook_before_add_ingredients(self):
        pass

    def hook_after_add_ingredients(self):
        pass

    def cut(self):
        print(f'Cutting {self.__class__.__name__} slices.')

    def serve(self):
        print(f'Serving {self.__class__.__name__}!')

    @abstractmethod
    def add_ingredients(self):
        pass

    @abstractmethod
    def cook(self):
        pass


class Pepperoni(Pizza):
    def hook_before_add_ingredients(self):
        print('cutting pepperoni slices.')

    def add_ingredients(self):
        print(f'Pizza of {self.__class__.__name__} needs pepperoni, mussarela, tomato sauce and oregano.')

    def cook(self):
        print(f'Cooking {self.__class__.__name__} for 5 minutes.')


class Mussarela(Pizza):
    def add_ingredients(self):
        print(f'Pizza of {self.__class__.__name__} needs mussarela, tomato sauce and oregano.')

    def cook(self):
        print(f'Cooking {self.__class__.__name__} for 2 minutes.')


if __name__ == '__main__':
    pizza_1 = Pepperoni()
    pizza_1.prepare()

    pizza_2 = Mussarela()
    pizza_2.prepare()
