import math

from algorithms import *
from functions import *

MATRIX=[
    [0, math.inf, math.inf, math.inf, 2, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf],
[math.inf, 0, 4, 4, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf],
[5, math.inf, 0, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf],
[math.inf, math.inf, math.inf, 0, math.inf, math.inf, math.inf, 8, math.inf, math.inf, math.inf, math.inf, math.inf, 8],
[math.inf, math.inf, math.inf, math.inf, 0, math.inf, 4, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf],
[math.inf, math.inf, math.inf, math.inf, math.inf, 0, 3, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf],
[math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, 0, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf],
[1, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, 0, math.inf, math.inf, math.inf, 1, math.inf, math.inf],
[math.inf, math.inf, math.inf, math.inf, math.inf, 3, math.inf, math.inf, 0, math.inf, math.inf, math.inf, math.inf, math.inf],
[math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, 0, math.inf, math.inf, math.inf, math.inf],
[math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, 4, math.inf, 0, math.inf, math.inf, math.inf],
[math.inf, math.inf, math.inf, math.inf, math.inf, 1, math.inf, math.inf, math.inf, math.inf, math.inf, 0, math.inf, math.inf],
[math.inf, math.inf, math.inf, math.inf, math.inf, 3, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, 0, math.inf],
[math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, 2, 0]
]

res, path = floyd_warshall(MATRIX, route=('B', 'G'), search='min')
print(f'Shortest path: {format_path(path)}')
