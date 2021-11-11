import os
import timeit
import random

# f = open("test.txt", "w")
# while (os.path.getsize('test.txt') / 1000000) < 50:
#     f.write(str(random.randint(1, 1000)) + '\n')

s = """
file = open("test.txt", "r")
result = 0
for line in file.readlines():
    if line.strip().isdigit():
        result+=int(line.strip())
file.close()
"""
print(timeit.timeit(s, number=5))

s = """
file = open("test.txt", "r")
result = 0
for line in file:
    if line.strip().isdigit():
        result+=int(line.strip())
file.close()
"""

print(timeit.timeit(s, number=5))

s = """
file = open("test.txt", "r")
result = sum(int(line.strip()) for line in file if line.strip().isdigit())
file.close()
"""
print(timeit.timeit(s, number=5))
