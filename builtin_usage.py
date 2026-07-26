import math
import random
import platform

# generate random integer, it's going to include 100
random_num = random.randint(1, 100)
print(f"Random number: {random_num}")

# get the sqrt and round down
random_sqrt = math.floor(math.sqrt(random_num))
print(f"Square root of {random_num} floored = {random_sqrt}")

# print system OS and Python version
print(f"Operating System: {platform.system()}")
print(f"Python Version: {platform.python_version()}")