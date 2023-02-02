class Vehicle:
    def __init__(self, vehicle_type: str) -> None:
        self.vehicle_type: str = vehicle_type

class Automobile(Vehicle):
    def __init__(self, vehicle_type: str) -> None:
        super().__init__(vehicle_type)
        self.year: int = 0
        self.make: str = ''
        self.model: str = ''
        self.doors: int = 2
        self.roof: str = 'solid'

car = Automobile(vehicle_type='car')
car.year = int(input('Enter the car year:'))
print(f"Vechicle type: {car.vehicle_type}")
