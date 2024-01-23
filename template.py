#####
# author: Your First and Last Name
#####

def get_name() -> str:
    # returns the user's name
    return input('Enter your name')

def add_two_numbers(num1: int, num2: int) -> int:
    """
        Add two numbers and return the result
    Args:
        num1 (int): number one
        num2 (int): number two

    Returns:
        int: the sum of num1 and num2
    """
    return num1 + num2

def is_first_greater_than_last(num1: int, num2: int) -> bool:
    """
        Determine if num1 is greater than num2
    Args:
        num1 (int): number one
        num2 (int): number two

    Returns:
        bool: true if num1 is greater, false otherwise
    """
    return num1 > num2


first_name: str = 'Ray'

# determine if the first_name has a value or not
if first_name:
    print(first_name)
else:
    print('first name is invalid')