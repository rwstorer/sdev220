"""
Demonstrate file input and output
"""

# First way - open the text file read-only
file = open('c:/temp/t.txt', 'rt')
# read the entire thing into RAM
file_lines: list = file.readlines()
file.close()
for line in file_lines:
    print(line)

# second way does not read the entire file into RAM
# and automatically closes it when done reading it.
with open('c:/temp/t.txt', 'rt') as file:
    for line in file:
        print(line, end='')

FILE_BEGIN: int = 0
FILE_CURRENT: int = 1
FILE_END: int = 2

# binary files
with open('c:/temp/t.bin', mode='rb') as file:
    file.seek(1, 0) # move forward one byte from the beginning
    print(file.tell()) # prints 1
    file.seek(-10, 2) # move ten bytes back from the end

# python mmap (memory mapped files)
# https://docs.python.org/3/library/mmap.html

# __str__() vs __repr__() / str() vs repr()
# https://www.geeksforgeeks.org/str-vs-repr-in-python/

try:
    file = open("file_name.txt", "rt")
    print(file.readline())
except FileNotFoundError:
    print("I didn't find the file")
    raise
finally:
    if file:
        file.close()
