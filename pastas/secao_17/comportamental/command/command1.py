from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Dict, List, Tuple


class Light:
    def __init__(self, name: str, room_name: str):
        self.name = name
        self.room_name = room_name
        self.color = 'white'

    def on(self):
        print(f'{self.name} in {self.room_name} is now on.')

    def off(self):
        print(f'{self.name} in {self.room_name} is now off.')

    def change_color(self, color: str):
        self.color = color
        print(f'{self.name} in {self.room_name} is now {self.color}.')


class ICommand(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass


class LightOnCommand(ICommand):
    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.on()

    def undo(self):
        self.light.off()


class LightChangeColor(ICommand):
    def __init__(self, light: Light, color: str):
        self.light = light
        self.color = color
        self._old_color = self.light.color

    def execute(self):
        self._old_color = self.light.color
        self.light.change_color(self.color)

    def undo(self):
        self.light.change_color(self._old_color)


class RemoteContoller:
    def __init__(self):
        self._buttons: Dict[str, ICommand] = {}
        self._undos: List[Tuple[str, str]] = []

    def button_add_command(self, button_name: str, command: ICommand):
        self._buttons[button_name] = command

    def button_pressed(self, button_name: str):
        if button_name in self._buttons:
            self._buttons[button_name].execute()
            self._undos.append((button_name, 'execute'))

    def button_undo(self, button_name: str):
        if button_name in self._buttons:
            self._buttons[button_name].undo()
            self._undos.append((button_name, 'undo'))

    def global_undo(self):
        if not self._undos:
            return print('Nothing to undo it.')
        button_name, action = self._undos[-1]
        if action == 'execute':
            self._buttons[button_name].undo()
        else:
            self._buttons[button_name].execute()

        self._undos.pop()


if __name__ == '__main__':
    bedroom_light = Light('Bedroom light 1', 'Bedroom')
    bathroom_light = Light('Bathroom light', 'Bathroom')

    bedroom_light_on = LightOnCommand(bedroom_light)
    bathroom_light_on = LightOnCommand(bathroom_light)
    bedroom_light_blue = LightChangeColor(bedroom_light, 'blue')
    bedroom_light_red = LightChangeColor(bedroom_light, 'red')

    remote_controller = RemoteContoller()
    remote_controller.button_add_command('first_button', bedroom_light_on)
    remote_controller.button_add_command('second_button', bathroom_light_on)
    remote_controller.button_add_command('third_button', bedroom_light_blue)
    remote_controller.button_add_command('fourth_button', bedroom_light_red)

    remote_controller.button_pressed('first_button')
    remote_controller.button_undo('first_button')

    remote_controller.button_pressed('second_button')
    remote_controller.button_undo('second_button')

    remote_controller.button_pressed('third_button')
    # remote_controller.button_undo('third_button')

    remote_controller.button_pressed('fourth_button')
    remote_controller.button_undo('fourth_button')

    print()
    remote_controller.global_undo()
    remote_controller.global_undo()
    remote_controller.global_undo()
    remote_controller.global_undo()
    remote_controller.global_undo()
    remote_controller.global_undo()
    remote_controller.global_undo()
    remote_controller.global_undo()
    remote_controller.global_undo()
