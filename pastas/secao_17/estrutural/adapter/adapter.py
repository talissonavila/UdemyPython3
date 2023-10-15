from abc import ABC, abstractmethod


class IControl(ABC):
    @abstractmethod
    def top(self): pass

    @abstractmethod
    def right(self): pass

    @abstractmethod
    def down(self): pass

    @abstractmethod
    def left(self): pass


class Control(IControl):
    def top(self):
        print('control Moving up')

    def right(self):
        print('control moving to right')

    def down(self):
        print('control moving down')

    def left(self):
        print('control moving left')


class NewControl:
    def move_top(self):
        print('new control Moving up')

    def move_right(self):
        print('new control moving to right')

    def move_down(self):
        print('new control moving down')

    def move_left(self):
        print('new control moving left')


class ControlAdapter:
    def __init__(self, new_control: NewControl):
        self.new_control = new_control

    def top(self):
        self.new_control.move_top()

    def right(self):
        self.new_control.move_right()

    def down(self):
        self.new_control.move_down()

    def left(self):
        self.new_control.move_left()


class ControlAdapter2(Control, NewControl):
    def top(self):
        self.move_top()

    def right(self):
        self.move_right()

    def down(self):
        self.move_down()

    def left(self):
        self.move_left()


if __name__ == '__main__':
    new_control_1 = NewControl()
    control_object = ControlAdapter(new_control_1)

    control_object.top()
    control_object.down()
    control_object.left()
    control_object.right()

    print()

    control_class = ControlAdapter2()
    control_class.top()
    control_class.left()
    control_class.right()
    control_class.down()
