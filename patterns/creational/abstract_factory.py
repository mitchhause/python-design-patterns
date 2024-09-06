from typing import Type


class Vehicle():
   def __init__(self, color: str, num_wheels: int) -> None:
       self.color = color
       self.num_wheels = num_wheels

   def honk_horn(self) -> None:
       raise NotImplemented

   def __str__(self) -> str:
       raise NotImplemented

   def get_brand(self)-> str:
       raise NotImplementedError


class Car(Vehicle):
    def honk_horn(self) -> None:
        print('honk')

    def __str__(self) -> str:
        return f"type: Car, color: {self.color}, num_wheels: {self.num_wheels}"

class Motorcycle(Vehicle):
    def honk_horn(self) -> None:
        print('beep')

    def __str__(self) -> str:
        return f"type: Motorcycle, color: {self.color}, num_wheels: {self.num_wheels}"

class FordCar(Car):
    def get_brand(self):
        return 'Ford'

class FordMotorcycle(Motorcycle):
    def get_brand(self):
        return 'Ford'

class VehicleFactory():
    def create_car(self) -> Type[Car]:
        raise NotImplemented
    def create_motorcycle(self) -> Type[Motorcycle]:
        raise NotImplemented

class FordFactory(VehicleFactory):
    def create_car(self):
        return FordCar
    def create_motorcyle(self):
        return FordMotorcycle

class Dealership():
    def __init__(self, v_factory: Type[VehicleFactory]) -> None:
        self.vehicle_factory = v_factory

    def buy_car(self, color: str, num_wheels: int):
        car = self.vehicle_factory().create_car()(color, num_wheels)


        print(f"here is your {car.get_brand()}")
        car.honk_horn()


if __name__ == '__main__':
    factory = FordFactory
    ford_dealership = Dealership(factory)

    ford_dealership.buy_car('blue', 3)
