from abc import ABC, abstractmethod


class UberBlack(ABC):
    @abstractmethod
    def search_client(self) -> None:
        pass

class UberX(ABC):
    @abstractmethod
    def search_client(self) -> None:
        pass

class CarUberBlackNorthZone(UberBlack):
    def search_client(self) -> None:
        return print("A Uber black car from North Zone it's searching client!")
    

class CarUberXNorthZone(UberX):
    def search_client(self) -> None:
        return print("A Uber X car from North Zone it's searching client.")


class BikeUberBlackNorthZone(UberBlack):
    def search_client(self) -> None:
        return print("A Uber black Bike from North Zone it's searching client!")


class BikeUberXNorthZone(UberX):
    def search_client(self) -> None:
        return print("A Uber X bike from North Zone it's searching client.")
    
class CarUberBlackSouthZone(UberBlack):
    def search_client(self) -> None:
        return print("A Uber black car from South Zone it's searching client!")
    
class CarUberXSouthZone(UberX):
    def search_client(self) -> None:
        return print("A Uber X car from South Zone it's searching client.")
    
class BikeUberBlackSouthZone(UberBlack):
    def search_client(self) -> None:
        return print("A Uber X bike from South Zone it's searching client.")
    
class BikeUberXSouthZone(UberX):
    def search_client(self) -> None:
        return print("A Uber X bike from South Zone it's searching client.")


class VehicleFactory(ABC):
    @staticmethod
    @abstractmethod
    def get_uber_black_car() -> UberBlack:
        pass

    @staticmethod
    @abstractmethod
    def get_uber_black_bike() -> UberBlack:
        pass
    
    @staticmethod
    @abstractmethod
    def get_uber_x_car() -> UberX:
        pass

    @staticmethod
    @abstractmethod
    def get_uber_x_bike() -> UberX:
        pass

class NorthZoneVehicleFactory(VehicleFactory):
    @staticmethod
    def get_uber_black_car() -> UberBlack:
        return CarUberBlackNorthZone()

    @staticmethod
    def get_uber_black_bike() -> UberBlack:
        return BikeUberBlackNorthZone()
    
    @staticmethod
    def get_uber_x_car() -> UberX:
        return CarUberXNorthZone()
    
    @staticmethod
    def get_uber_x_bike() -> UberX:
        return BikeUberXNorthZone()

class SouthZoneVehicleFactory(VehicleFactory):
    @staticmethod
    def get_uber_black_car() -> UberBlack:
        return CarUberBlackSouthZone()

    @staticmethod
    def get_uber_black_bike() -> UberBlack:
        return BikeUberBlackSouthZone()
    
    @staticmethod
    def get_uber_x_car() -> UberX:
        return CarUberXSouthZone()
    
    @staticmethod
    def get_uber_x_bike() -> UberX:
        return BikeUberXSouthZone()


class Client:
    def get_clients(self):
        for factory in [NorthZoneVehicleFactory(), SouthZoneVehicleFactory()]:
            uber_x_car = factory.get_uber_x_car()
            uber_x_car.search_client()

            uber_vip_car = factory.get_uber_black_car()
            uber_vip_car.search_client()

            uber_x_bike = factory.get_uber_x_bike()
            uber_x_bike.search_client()

            uber_black_bike = factory.get_uber_black_bike()
            uber_black_bike.search_client()


if __name__ == "__main__":
    client = Client()
    client.get_clients()        