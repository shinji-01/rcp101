# {{{
# Soit M la matrice d'adjacence à n sommets et M' la matrice d'adjacence de la fermeture transitive du graphe.
# Alors, M' = M + M^2 + ... + M^n

# Prenons le graphe suivant ayant pour matrice d'adjacence:
#
# A──────────────► C────┐
# ▲                │    │
# └────────────────┘    │
#                       │
#                 B◄────┘

# (0, 0, 1)
# (0, 0, 0)
# (1, 1, 0)

# Pour réaliser la fermeture transitive, il nous faut déterminer quelles sont les adjacences par transitivités. Par exemple, il est possible d'aller de A à B en faisant A->C->B. Nous pouvons donc définir une adjacence entre A et B.
# ┌───A──────────────► C────┐
#     ▲                │    │
# │   └────────────────┘    │
#                           │
# │                         │
#                           │
# └ ─ ─ ─ ─ ─ ─ ─ ─ ─►B◄────┘

# Notre matrice ressemble donc à
# (0, 1, 1)
# (0, 0, 0)
# (1, 1, 0)

# De la même manière, nous pouvons aller à A en faisant A->C->A. Ce qui s'apparente à une boucle. Nous pouvons également aller à C en faisant C->A->C.
#
#     ┌ ─┐             ┌ ─┐
#     ▼                ▼   
#     ┌ ─┘             ┌ ─┘
#     │                │
# ┌───A──────────────► C────┐
#     ▲                │    │
# │   └────────────────┘    │
#                           │
# │                         │
#                           │
# └  ─── ─── ─── ── ─►B◄────┘

# Notre matrice ressemble donc à
# (1, 1, 1)
# (0, 0, 0)
# (1, 1, 1)

# }}}

from copy import deepcopy
import math, string
from functions import *

def transitive_closure(matrix):
    identity_matrix = construct_identity(len(matrix))

    mi = add(matrix, identity_matrix)

    res = deepcopy(mi)

    iteration = 1

    for n in range(len(matrix)):
        before = deepcopy(res)

        res = multiply(mi, res)
        res = binarize(res)

        after = deepcopy(res)
        iteration = iteration + 1

        if not has_changed(before, after):
            return res, iteration - 1


    return res, iteration


# Pour obtenir les distances les plus courtes pour chaque points
# /!\ Ne marche pas si le graphe comporte un cycle ayant une somme négative
def bellman_ford(matrix):
    edge_list = get_edges(matrix)
    length = len(matrix)

    distances = [0] + [math.inf for i in range(length - 1)]

    for iteration in range(length - 1):
        for edge in edge_list:
            # sommet
            vertex_from = edge[0]
            vertex_to = edge[1]

            value = matrix[vertex_from][vertex_to]

            new_distance = distances[vertex_from] + value

            if new_distance < distances[vertex_to]:
                distances[vertex_to] = new_distance

    return distances

# Pour obtenir une matrice des plus courts chemins par arc.
def floyd_warshall(matrix, route=None, search='min'):
    # shortest path matrix
    sp_matrix = deepcopy(matrix)

    # path reconstruction matrix
    pr_matrix = [[None]*len(matrix) for i in range(len(matrix))]

    for i in range(len(matrix)):
        pr_matrix[i][i] = i
        for j in range(len(matrix)):
            pr_matrix[i][j] = j

    for k in range(len(matrix)):
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if i == k or j == k or i == j:
                    continue

                if search == 'min':
                    if sp_matrix[i][j] > sp_matrix[i][k] + sp_matrix[k][j]:
                        sp_matrix[i][j] = sp_matrix[i][k] + sp_matrix[k][j]
                        pr_matrix[i][j] = pr_matrix[i][k]
                else:
                    if sp_matrix[i][j] < sp_matrix[i][k] + sp_matrix[k][j]:
                        sp_matrix[i][j] = sp_matrix[i][k] + sp_matrix[k][j]

    if route is not None:
        converted_route = (string.ascii_uppercase.index(route[0]), string.ascii_uppercase.index(route[1]))
        shortest_path = path_reconstruction(pr_matrix, converted_route)

        return sp_matrix, shortest_path

    return sp_matrix

def simplexe(matrix, coefs, base, solutions, debug=False):
    width = len(matrix[0]) - 1
    height = len(matrix) - 1

    if debug:
        print('Problem expression:')
        print_linear_problem(matrix, coefs)

    # Convert values of matrix to float
    for i in range(height + 1):
        for j in range(width + 1):
            matrix[i][j] = float(matrix[i][j])

    next_matrix = deepcopy(matrix)

    while max(next_matrix[height]) > 0:
        matrix_tmp = deepcopy(next_matrix)

        # step 3: Choisir les variables à introduire dans la base
        # On détermine la colonne du pivot c en prenant la valeur maximum dans la ligne Z.
        # On prend la colonne ayant la valeur maximum dans la ligne Z (fonction à optimiser)
        p_column = matrix_tmp[height].index(max(matrix_tmp[height]))

        # step 4: Choisir la variable à enlever de la base
        # On divise les valeurs de la solution B par les valeurs dans la colonne du pivot et on choisit la valeur minimale positive.
        # Les valeurs de la solution B sont mise en bout de ligne. (ex: x1 + 2x2 = 230 => [1, 2, 230])
        # Si notre pivot est la première ligne (matrix[0]) nous devons donc choisir la plus petite valeur parmis
        # La ligne ayant la valeur minimale sera nommé "ligne pivot"
        compute_line = []

        for i in range(height):
            if matrix_tmp[i][p_column] > 0:
                compute_line.append(matrix_tmp[i][width] / matrix_tmp[i][p_column])
            else:
                compute_line.append(math.inf)

        p_line = compute_line.index(min(compute_line))

        base[p_line] = coefs[p_column]

        # step 5: Encadrer le pivot
        pivot = matrix_tmp[p_line][p_column]

        # step 6: diviser la ligne du pivot par le pivot
        for j in range(width + 1):
            next_matrix[p_line][j] = matrix_tmp[p_line][j] / pivot

        # step 7: calculer les valeurs des autres lignes
        # La valeur calculée sera nommé E
        for i in range(height + 1):
            if i == p_line:
                continue

            for j in range(width + 1):
                next_matrix[i][j] = matrix_tmp[i][j] - (matrix_tmp[i][p_column] / pivot) * matrix_tmp[p_line][j]

    # L'algorithme s'arrête si les valeurs des coefficients dans la fonction objectif sont négatifs ou nul
    print('\nSolution:')

    for solution in solutions:
        print(f'{solution} = {next_matrix[base.index(solution)][width]}')
