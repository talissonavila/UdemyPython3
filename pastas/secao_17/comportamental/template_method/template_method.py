from abc import ABC, abstractmethod


class Abstract(ABC):
    def tempate_method(self):
        self.hook()
        self.operation1()
        self.base_class_method()
        self.operation2()

    def hook(self):
        pass

    def base_class_method(self):
        print('Hello, I am from abstract class and I will be executed as well.')

    @abstractmethod
    def operation1(self):
        pass

    @abstractmethod
    def operation2(self):
        pass


class ConcreteClass1(Abstract):
    def hook(self):
        print('HOOK CC1')

    def operation1(self):
        print(f'Operation 1 concluded.')

    def operation2(self):
        print(f'Operation 2 concluded.')


class ConcreteClass2(Abstract):
    def operation1(self):
        print(f'Operation 1 semi-concluded.')

    def operation2(self):
        print(f'Operation 2 semi-concluded.')


if __name__ == '__main__':
    concrete1 = ConcreteClass1()
    concrete1.tempate_method()

    concrete2 = ConcreteClass2()
    concrete2.tempate_method()
