from time import sleep
from math import sqrt

x = float(input())
miliseconds = float(input())

sleep(miliseconds/1000)

print(f'Square root of {int(x)} after {int(miliseconds)} miliseconds is {sqrt(x)}')