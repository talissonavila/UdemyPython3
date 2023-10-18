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
    def __init__(self, hotdog: Hotdog, ingredient: Ingredient):
        self.hotdog = hotdog
        self._ingredient = ingredient

        self._ingredients = deepcopy(self.hotdog.ingredients)
        self.ingredients.append(self._ingredient)

    @property
    def name(self) -> str:
        return f'{self.hotdog.name} + {self._ingredient.__class__.__name__}'


if __name__ == '__main__':
    simple_hotdog = SimpleHotDog()
    print(simple_hotdog)

    simple_hotdog_with_bacon = HotDogDecorator(simple_hotdog, Bacon())
    simple_hotdog_with_eggbacon = HotDogDecorator(simple_hotdog_with_bacon, Egg())
    mashed_potato_simple_hot_dog = HotDogDecorator(simple_hotdog, MashedPotatoes())

    print(simple_hotdog_with_bacon)
    print(simple_hotdog_with_eggbacon)
    print(mashed_potato_simple_hot_dog)
