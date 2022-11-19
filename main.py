from algorithms import *

MATRIX = [
    [0, 4, 0, 5],
    [0, 0, 0, 5],
    [0, -10, 0, 0],
    [0, 0, 3, 0],
]

print(bellman_ford(MATRIX))
