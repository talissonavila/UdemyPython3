from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Dict, List


class IObservable(ABC):
    """Observable abstract interface class."""

    @property
    @abstractmethod
    def state(self):
        pass

    @abstractmethod
    def add_observer(self, observer: IObserver):
        pass

    @abstractmethod
    def remove_observer(self, observer: IObserver):
        pass

    @abstractmethod
    def notify_observers(self):
        pass


class WeatherStation(IObservable):
    """Weather Station Class."""

    def __init__(self):
        self._observers: List[IObserver] = []
        self._state: Dict = {}

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state_update: Dict):
        new_state: Dict = {**self._state, **state_update}

        if new_state != self._state:
            self._state = new_state
            self.notify_observers()

    def reset_state(self):
        self._state = {}
        self.notify_observers()

    def add_observer(self, observer: IObserver):
        self._observers.append(observer)

    def remove_observer(self, observer: IObserver):
        if observer not in self._observers:
            return

        self._observers.remove(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.update()
        print()


class IObserver(ABC):
    """Observer abstract interface class."""

    @abstractmethod
    def update(self):
        pass


class Smartphone(IObserver):
    def __init__(self, name, observable: IObservable):
        self.name = name
        self.observable = observable

    def update(self):
        observable_name = self.observable.__class__.__name__
        print(f'{self.name}, the object {observable_name} updated to {self.observable.state}.')


class Notebook(IObserver):
    def __init__(self, observable: IObservable):
        self.observable = observable

    def show(self):
        print(f'Notebook does other things with data.', self.observable.state)

    def update(self):
        self.show()


class WeatherStationFacade:
    def __init__(self):
        self.weather_station = WeatherStation()

        self.redmi_note_9 = Smartphone('Redmi Note 9', self.weather_station)
        self.iphone_8_plus = Smartphone('iPhone 8 Plus', self.weather_station)

        self.notebook = Notebook(self.weather_station)

        self.weather_station.add_observer(self.redmi_note_9)
        self.weather_station.add_observer(self.iphone_8_plus)
        self.weather_station.add_observer(self.notebook)

    def add_observer(self, observer: IObserver):
        self.weather_station.add_observer(observer)

    def remove_observer(self, observer: IObserver):
        self.weather_station.remove_observer(observer)

    def change_state(self, state: Dict):
        self.weather_station.state = state

    def remove_redmi_note_9(self):
        self.weather_station.remove_observer(self.redmi_note_9)

    def reset_state(self):
        self.weather_station.reset_state()


if __name__ == '__main__':
    weather_station = WeatherStationFacade()

    weather_station.change_state({'temperature': '30 degrees celcius'})
    weather_station.change_state({'temperature': '32 degrees celcius'})
    weather_station.change_state({'humidity': '75%'})

    weather_station.remove_redmi_note_9()
    weather_station.reset_state()

    weather_station.change_state({'temperature': '30 degrees celcius'})
