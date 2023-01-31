"""
Name     : Your name goes here
File Name: m02_lab_case_study.py
Summary  : Summary of code purpose goes here
"""

NAME_PROMPT: str = 'Enter your name'
GPA_PROMPT: str = 'Enter your GPA'
MIN_NAME_LEN: int = 3
MIN_NAME_LEN_ERR: str = f"Minimum name length is: {MIN_NAME_LEN}"
TRY_AGAIN_ERR: str = 'Please try again'
FLOAT_ERR: str = 'Please input a floating point number'

user_name: str = ''
while True:
    user_name = input(NAME_PROMPT)
    if len(user_name) >= MIN_NAME_LEN:
        break
    else:
        print(MIN_NAME_LEN_ERR)
        print(TRY_AGAIN_ERR)

while True:
    try:
        gpa: float = float(input(GPA_PROMPT))
        break
    except:
        print(FLOAT_ERR)



child_ages: dict = {
    'Fred'   : 10,
    'Barney' : 9
}

test: str = 'one'
def mangle(arg: str) -> str:
    global test
    arg = 'two'
    test = arg
    return arg

print(test)
mangle(test)
print(test)
