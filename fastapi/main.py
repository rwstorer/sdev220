"""
    author:
    assignment:
    version: 1.2
    history:
      ver   who when what
      --    ----  --- ---
"""

SHORT_PIE: float = 3.1415927


first_name: str = 'fred'

names: dict = {
    'first': 'fred',
}

def some_function() -> int:
    i: int = 0

    return i


class someClass:
    first_name: str = None



def main(item1: str, item2: int) -> int:
    """this function does ...

    Args:
        item1 (str): name of the dog
        item2 (int): age of the dog

    Returns:
        int: dog age in human years
    """

    if item1 == 'Fred': # determine the dog's name
        print('Hi, Fred')