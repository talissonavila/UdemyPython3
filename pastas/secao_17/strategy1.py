from __future__ import annotations
from abc import abstractmethod, ABC


class Order:
    def __init__(self, total: float, discount: DiscountStrategy):
        self._total = total
        self._discount = discount

    @property
    def total(self):
        return self._total

    @property
    def total_with_discount(self):
        return self._discount.calculate(self.total)


class DiscountStrategy(ABC):
    @abstractmethod
    def calculate(self, value: float) -> float:
        pass


class TwentyPercent(DiscountStrategy):
    def calculate(self, value: float) -> float:
        return value - (value * 0.2)


class FiftyPercent(DiscountStrategy):
    def calculate(self, value: float) -> float:
        return value - (value * 0.5)


class NoDiscount(DiscountStrategy):
    def calculate(self, value: float) -> float:
        return value


class CustomDiscountPercent(DiscountStrategy):
    def __init__(self, discount):
        self.discount = discount / 100

    def calculate(self, value: float) -> float:
        return value - (value * self.discount)


if __name__ == '__main__':
    discount_of_20_percent = TwentyPercent()
    order = Order(1000, discount_of_20_percent)
    print(order.total, order.total_with_discount)

    discount_of_50_percent = FiftyPercent()
    order2 = Order(1000, discount_of_50_percent)
    print(order2.total, order2.total_with_discount)

    no_discount = NoDiscount()
    order3 = Order(1000, no_discount)
    print(order3.total, order3.total_with_discount)

    discount_of_3_percent = CustomDiscountPercent(3)
    order4 = Order(1000, discount_of_3_percent)
    print(order4.total, order4.total_with_discount)
    