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
    def __init__(self) -> None:
        self.color: str = ''
        self.transmission: str = 'automatic'

class Yugo(Car):
    def __init__(self) -> None:
        super().__init__()
        self.color = 'white'
        self.transmission = 'manual'
    def __str__(self) -> str:
        return 'Color: ' + self.color + 'transmission: ' + self.transmission










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