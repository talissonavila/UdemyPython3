from __future__ import annotations
from abc import ABC, abstractmethod


class IRemoteControl(ABC):
    @abstractmethod
    def increase_volume(self):
        pass

    @abstractmethod
    def decrease_volume(self):
        pass

    @abstractmethod
    def power(self):
        pass


class RemoteControl(IRemoteControl):
    def __init__(self, device: IDevice):
        self._device = device

    def increase_volume(self):
        self._device.volume += 1

    def decrease_volume(self):
        self._device.volume -= 1

    def power(self):
        self._device.power = not self._device.power


class RemoteControlWithMute(IRemoteControl):
    def __init__(self, device: IDevice):
        self._device = device

    def increase_volume(self):
        self._device.volume += 1

    def decrease_volume(self):
        self._device.volume -= 1

    def power(self):
        self._device.power = not self._device.power

    def mute(self):
        self._device.volume = 0


class IDevice(ABC):
    @property
    @abstractmethod
    def volume(self) -> int:
        pass

    @volume.setter
    def volume(self, volume: int):
        pass

    @property
    @abstractmethod
    def power(self) -> bool:
        pass

    @power.setter
    def power(self, power: bool):
        pass


class TV(IDevice):
    def __init__(self):
        self._volume = 10
        self._power = False
        self._name = self.__class__.__name__

    @property
    def volume(self) -> int:
        return self._volume

    @volume.setter
    def volume(self, volume: int):
        if not self.power:
            print(f'{self._name} is off. Turn on.')
            return
        if volume > 100:
            return
        if volume < 0:
            return

        self._volume = volume
        print(f'Volume is on {self._volume}.')

    @property
    def power(self) -> bool:
        return self._power

    @power.setter
    def power(self, power: bool):
        self._power = power
        power_status = 'ON' if self._power else 'OFF'
        print(f'{self._name} is now {power_status}.')


class Radio(IDevice):
    def __init__(self):
        self._volume = 10
        self._power = False
        self._name = self.__class__.__name__

    @property
    def volume(self) -> int:
        return self._volume

    @volume.setter
    def volume(self, volume: int):
        if not self.power:
            print(f'{self._name} is off. Turn on.')
            return
        if volume > 100:
            return
        if volume < 0:
            return

        self._volume = volume
        print(f'Volume is on {self._volume}.')

    @property
    def power(self) -> bool:
        return self._power

    @power.setter
    def power(self, power: bool):
        self._power = power
        power_status = 'ON' if self._power else 'OFF'
        print(f'{self._name} is now {power_status}.')


if __name__ == '__main__':
    tv = TV()
    remote_control = RemoteControl(tv)

    remote_control.increase_volume()
    remote_control.power()
    remote_control.increase_volume()
    remote_control.increase_volume()
    remote_control.increase_volume()
    remote_control.increase_volume()
    remote_control.decrease_volume()
    remote_control.decrease_volume()
    remote_control.decrease_volume()
    remote_control.power()
    remote_control.decrease_volume()

    print('--' * 30)

    radio = Radio()
    remote_control_radio = RemoteControl(radio)

    remote_control_radio.increase_volume()
    remote_control_radio.power()
    remote_control_radio.increase_volume()
    remote_control_radio.increase_volume()
    remote_control_radio.increase_volume()
    remote_control_radio.increase_volume()
    remote_control_radio.decrease_volume()
    remote_control_radio.decrease_volume()
    remote_control_radio.decrease_volume()
    remote_control_radio.power()
    remote_control_radio.decrease_volume()

    print('--' * 30)

    radio2 = Radio()
    remote_control_radio2 = RemoteControlWithMute(radio2)
    remote_control_radio2.power()
    remote_control_radio2.increase_volume()
    remote_control_radio2.mute()
