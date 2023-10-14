from __future__ import annotations
from abc import ABC, abstractmethod


class Order:
    def __init__(self):
        self.state: OrderState = PaymentPending(self)

    def pending(self):
        self.state.pending()

    def approve(self):
        self.state.approve()

    def reject(self):
        self.state.reject()


class OrderState(ABC):
    def __init__(self, order: Order):
        self.order = order

    @abstractmethod
    def pending(self):
        pass

    @abstractmethod
    def approve(self):
        pass

    @abstractmethod
    def reject(self):
        pass


class PaymentPending(OrderState):
    def __init__(self, order: Order):
        self.order = order

    def pending(self):
        print('Payment already in pending. Passing.')

    def approve(self):
        self.order.state = PaymentApproved(self.order)
        print('Payment approved.')

    def reject(self):
        self.order.state = PaymentRejected(self.order)
        print('Payment rejected.')


class PaymentApproved(OrderState):
    def __init__(self, order: Order):
        self.order = order

    def pending(self):
        self.order.state = PaymentPending(self.order)
        print('Payment pending.')

    def approve(self):
        print('Payment already approved. Passing.')

    def reject(self):
        self.order.state = PaymentRejected(self.order)
        print('Payment refused.')


class PaymentRejected(OrderState):
    def __init__(self, order: Order):
        self.order = order

    def pending(self):
        print('Payment already refused.')

    def approve(self):
        print('Payment already refused.')

    def reject(self):
        print('Payment already refused.')


if __name__ == '__main__':
    order1 = Order()
    order1.pending()
    order1.approve()
    order1.pending()
    order1.reject()
    order1.pending()
    order1.approve()
    