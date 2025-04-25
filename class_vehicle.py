class Vehicle:
    def __init__(self, vehicle_type: str) -> None:
        self.vehicle_type: str = vehicle_type
        #TODO: constrain vehicle_type
    
    def __str__(self):
        return self.vehicle_type

class Automobile(Vehicle):
    def __init__(self, vehicle_type: str, year: int, make: str, model: str, doors: int, roof: str) -> None:
        super().__init__(vehicle_type)
        self.year: int = year
        self.make: str = make
        self.model: str = model
        self.doors: int = doors
        self.roof: str = roof
        #TODO: constrain door to 2 or 4 and roof to solid or sun
        
    def __str__(self):.
        return ( f"Vehicle Type: {super().__str__()}\n" +
            f"Year: {self.year}\n" +
            f"Make: {self.make}\n" +
            f"Model: {self.model}\n" +
            f"Doors: {self.doors}\n" +
            f"Roof: {self.roof}"
        )

vehicle_type: str = "car"
# TODO: get inputs
make: str = 'Toyota'
model: str = 'Rav4'
year: int = 2025
doors: int = 4
roof: str = 'sun'
car = Automobile(vehicle_type=vehicle_type, 
                 make=make, 
                 model=model,
                 year=year,
                 doors=doors, 
                 roof=roof)
print(car)
