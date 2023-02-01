# lambda example
yes_no_odd = lambda num: f"Yes, the number {num} is odd" if num % 2 > 0 else f"No, the number {num} is not odd"
is_odd = lambda num: num % 2 > 0

some_num: int = 3

print(yes_no_odd(some_num))

if is_odd(some_num):
    print(f"Yes, {some_num} is odd")
else:
    print(f"No, {some_num} is not odd")
