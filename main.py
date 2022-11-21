import math

from algorithms import *
from functions import *

I = math.inf

MATRIX = [
    [0, I, I, I, 2, I, I, I, I, I, I, I, I, I],
    [I, 0, 4, 4, I, I, I, I, I, I, I, I, I, I],
    [5, I, 0, I, I, I, I, I, I, I, I, I, I, I],
    [I, I, I, 0, I, I, I, 8, I, I, I, I, I, 8],
    [I, I, I, I, 0, I, 4, I, I, I, I, I, I, I],
    [I, I, I, I, I, 0, 3, I, I, I, I, I, I, I],
    [I, I, I, I, I, I, 0, I, I, I, I, I, I, I],
    [1, I, I, I, I, I, I, 0, I, I, I, 1, I, I],
    [I, I, I, I, I, 3, I, I, 0, I, I, I, I, I],
    [I, I, I, I, I, I, I, I, I, 0, I, I, I, I],
    [I, I, I, I, I, I, I, I, 4, I, 0, I, I, I],
    [I, I, I, I, I, 1, I, I, I, I, I, 0, I, I],
    [I, I, I, I, I, 3, I, I, I, I, I, I, 0, I],
    [I, I, I, I, I, I, I, I, I, I, I, I, 2, 0]
]

#res, path = floyd_warshall(MATRIX, route=('B', 'G'), search='min')
#print(f'Shortest path: {format_path(path)}')

MATRIX = [
    [3, 2, 1, 0, 0, 1800],
    [1, 0, 0, 1, 0, 400],
    [0, 1, 0, 0, 1, 600],
    [30, 50, 0, 0, 0, 0] # Z
]

simplexe(
    MATRIX,
    coefs = ['x1', 'x2', 'x3', 'x4', 'x5'],
    base = ['x3', 'x4', 'x5'],
    solutions = ['x1', 'x2'],
    debug = True
)

