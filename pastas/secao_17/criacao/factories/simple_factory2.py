from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def search_client(self) -> None:
        pass


class VehiculeVIP(Vehicle):
    def search_client(self) -> None:
        return print("Vip car its searching client!")
    

class VehicleNormal(Vehicle):
    def search_client(self) -> None:
        return print("Normal car its searching client.")


class SpecialBike(Vehicle):
    def search_client(self) -> None:
        return print("Special Bike its searching client!")


class RegularBike(Vehicle):
    def search_client(self) -> None:
        return print("Regular bike its searching client.")


class FactoryVehicle:
    def __init__(self, option: str) -> None:
        self.vehicle = self.get_vehicle(option)

    @staticmethod
    def get_vehicle(option: str) -> Vehicle:
        if option == "vip_car":
            return VehiculeVIP()
        elif option == "normal_car":
            return VehicleNormal()
        elif option == "special_bike":
            return SpecialBike()
        elif option == "regular_bike":
            return RegularBike()
        assert 0, "Vehicle doesn't exists."

    def search_client(self):
        self.vehicle.search_client()


if __name__ == "__main__":
    from random import choice
    available_cars = ["vip_car", "normal_car", "special_bike", "regular_bike"]

    for i in range(10):
        car = FactoryVehicle(choice(available_cars))
        car.search_client()
