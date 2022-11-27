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

#MATRIX = [
#    [1, 1, 1, -1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1000],
#    [1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4000],
#    [0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 2000],
#    [1, 0, 1, 0, 0, 0, -1, 0, 0, 0, 0, 1, 0, 0, 500],
#    [1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 4000],
#    [1, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 1, 0, 1500],
#    [0, 0, 1, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 1, 1500],
#]
#
##print_matrix(MATRIX, headers=['x1', 'x2', 'x3', 'x4', 'x5', 'B'], base=['x3', 'x4', 'x5', 'Z'])
#simplexe(
#    MATRIX,
#    coefs = ['x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7', 'x8', 'x9', 'x10', 'x11', 'x12', 'x13', 'x14', 'B'],
#    base = ['x4', 'x5', 'x6', 'x7', 'x8', 'x9', 'x10', 'x11', 'x12', 'x13', 'x14', 'Z'],
#    solutions = [],
#    debug = True
#)

MATRIX = [
    [2, 1, 1, 0, 0, 18],
    [2, 3, 0, 1, 0, 42],
    [3, 1, 0, 0, 1, 24],
    [3, 2, 0, 0, 0, 0],
]

#print_matrix(MATRIX, headers=['x1', 'x2', 'x3', 'x4', 'x5', 'B'], base=['x3', 'x4', 'x5', 'Z'])
simplexe(
    MATRIX,
    coefs = ['x1', 'x2', 'x3', 'x4', 'x5', 'B'],
    base = ['x3', 'x4', 'x5', 'Z'],
    solutions = ['x1', 'x2'],
    debug = True
)
