class Vehicle:
    def __init__(self, vehicle_type: str):
        self.vehicle_type: str = vehicle_type
        # TODO: car, truck, plane, boat, or a broomstick


class Automobile(Vehicle):
    def __init__(self, year: int, make: str, model: str, doors: int, roof: str):
        super().__init__()
        self.year
        self.make
        self.model
        self.doors #TODO: 2 or 4
        self.roof  #TODO: solid or sun
        
    def __str__(self):
        f"""Vehicle type: {self.car
        Year: 2022
  Make: Toyota
  Model: Corolla
  Number of doors: 4
  Type of roof: sun roof
        me: str = 
        
vehicle_type: str = input("What is your vehicle type? ")
car = Automobile(vehicle_type=vehicle_type)