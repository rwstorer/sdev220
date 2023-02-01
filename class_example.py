# class examples
class shape:
    def __init__(self) -> None:
        self.num_sides: int = 0
    
    def __eq__(self, __o: object) -> bool:
        pass

    def __str__(self) -> str:
        pass

class square(shape):
    def __init__(self) -> None:
        super().__init__()

    def __eq__(self, __o: object) -> bool:
        return super().__eq__(__o)

    def __str__(self) -> str:
        return super().__str__()