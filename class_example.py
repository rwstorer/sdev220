# class examples
class A():
    count = 0
    def __init__(self):
        A.count += 1
    def exclaim(self):
        print("I'm an A!")
    @classmethod
    def kids(cls):
        print("A has", cls.count, "little objects.")

a1 = A()
a2 = A()
a3 = A()




class Car:
    def __init__(self, color: str, transmission: str) -> None:
        self.color: str = color
        self.transmission: str = transmission


class Yugo(Car):
    def __init__(self, color: str, transmission: str, shifter) -> None:
        super().__init__(color, transmission)
        self.shifter: str = shifter

    def __str__(self) -> str:
        return 'Color: ' + self.color + 'transmission: ' + self.transmission + ' shifter: ' + self.shifter


my_yugo = Yugo('blue', 'manual', 'floor')

print(my_yugo)










class Cat:
    def __init__(self, name, nemesis, age) -> None:
        self.name: str = name
        self.nemesis: str = nemesis
        self.age: float = age

my_cat = Cat(name='ted', nemesis='fred', age=1.5)
my_cat.name



class MyShape:    
    def __init__(self) -> None:
        self.num_sides: int = 0
    
    def __eq__(self, __o: object) -> bool:
        pass

    def __str__(self) -> str:
        pass

class MySquare(MyShape):
    def __init__(self) -> None:
        super().__init__()

    def __eq__(self, __o: object) -> bool:
        return super().__eq__(__o)

    def __str__(self) -> str:
        return super().__str__()


class Vehicle():
    def __init__(self, vehicle_type: str) -> None:
        self.vehicle_type: str = vehicle_type

class Automobile(Vehicle):
    def __init__(self,
                 vehicle_type: str,
                 year: int,
                 make: str,
                 model: str,
                 door: int, roof: str) -> None:
        super().__init__(vehicle_type)
        self.year: int = year
        self.make: str = make
        self.model: str = model
        self.door: int = door
        self.roof: str = roof
