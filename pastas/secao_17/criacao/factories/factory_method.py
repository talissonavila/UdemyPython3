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


class VehicleFactory(ABC):
    def __init__(self, option: str) -> None:
        self.vehicle = self.get_vehicle(option)

    @staticmethod
    @abstractmethod
    def get_vehicle(option: str) -> Vehicle:
        pass

    def search_client(self):
        self.vehicle.search_client()

class NorthZoneVehicleFactory(VehicleFactory):
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

class SouthZoneVehicleFactory(VehicleFactory):
    @staticmethod
    def get_vehicle(option: str) -> Vehicle:
        if option == "normal_car":
            return VehicleNormal()
        elif option == "regular_bike":
            return RegularBike()
        assert 0, "Vehicle doesn't exists."


if __name__ == "__main__":
    from random import choice
    north_zone_available_vehicles = ["vip_car", "normal_car", "special_bike", "regular_bike"]
    south_zone_available_vehicles = ["normal_car", "regular_bike"]

    for i in range(10):
        car = NorthZoneVehicleFactory(choice(north_zone_available_vehicles))
        car.search_client()

    print('-'*30)

    for i in range(10):
        vehicle = SouthZoneVehicleFactory(choice(south_zone_available_vehicles))
        vehicle.search_client()
        