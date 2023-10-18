from __future__ import annotations
from dataclasses import dataclass
from typing import List
from copy import deepcopy


@dataclass
class Ingredient:
    price: float


@dataclass
class Bread(Ingredient):
    price: float = 1.5


@dataclass
class Sausage(Ingredient):
    price: float = 4.99


@dataclass
class Bacon(Ingredient):
    price: float = 7.50


@dataclass
class Egg(Ingredient):
    price: float = 1.25


@dataclass
class Cheese(Ingredient):
    price: float = 2


@dataclass
class MashedPotatoes(Ingredient):
    price: float = 3


@dataclass
class PotatoSticks(Ingredient):
    price: float = 1.1


class Hotdog:
    _name: str
    _ingredients: List[Ingredient]

    @property
    def price(self) -> float:
        return round(sum([
            ingredient.price for ingredient in self._ingredients
        ]), 2)

    @property
    def name(self) -> str:
        return self._name

    @property
    def ingredients(self) -> List[Ingredient]:
        return self._ingredients

    def __repr__(self) -> str:
        return f'{self.name}: R${self.price} - {self.ingredients}'


class SimpleHotDog(Hotdog):
    def __init__(self):
        self._name = 'Simple Hot Dog'
        self._ingredients: List[Ingredient] = [
            Bread(),
            Sausage(),
            PotatoSticks()
        ]


class SpecialHotDog(Hotdog):
    def __init__(self):
        self._name = 'Special Hot Dog'
        self._ingredients = [
            Bread(),
            Sausage(),
            Bacon(),
            Egg(),
            Cheese(),
            PotatoSticks(),
            MashedPotatoes()
        ]


class HotDogDecorator(Hotdog):
    def __init__(self, hotdog: Hotdog):
        self.hotdog = hotdog

    @property
    def price(self) -> float:
        return self.hotdog.price

    @property
    def name(self) -> str:
        return self.hotdog.name

    @property
    def ingredients(self) -> List[Ingredient]:
        return self.hotdog.ingredients


class SimpleHotDogWithBacon(HotDogDecorator):
    def __init__(self, hotdog: Hotdog):
        super().__init__(hotdog)

        self._ingredient = Bacon()
        self._ingredients = deepcopy(self.hotdog.ingredients)
        self._ingredients.append(self._ingredient)

    @property
    def price(self) -> float:
        return round(sum([
            ingredient.price for ingredient in self._ingredients
        ]), 2)

    @property
    def name(self) -> str:
        return f'{self.hotdog.name} + {self._ingredient.__class__.__name__}'

    @property
    def ingredients(self) -> List[Ingredient]:
        return self._ingredients


if __name__ == '__main__':
    hotdog1 = SimpleHotDog()

    decorated_simple_hotdog = HotDogDecorator(hotdog1)

    hotdog2 = SimpleHotDogWithBacon(hotdog1)
    hotdog2 = SimpleHotDogWithBacon(hotdog2)
    print(hotdog2)
