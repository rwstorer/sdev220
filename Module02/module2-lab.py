"""
Your Name Goes Here
The file name goes here
Describe the function of the program
"""

DEANS_LIST: float = 3.5
HONOR_ROLL: float = 3.25
SENTINEL: str = 'ZZZ'
gpa: float = 0.0
first_name: str = ''
last_name: str = ''

while last_name != SENTINEL:
    last_name = input('Enter last name (ZZZ to quit):')
    if last_name == SENTINEL:
        break
    gpa = input('Enter student GPA:')
    try:
        gpa = float(gpa)
    except ValueError:
        continue
    if gpa >= DEANS_LIST:
        print()
    elif gpa >= HONOR_ROLL:
        print()
