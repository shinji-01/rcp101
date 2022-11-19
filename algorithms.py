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
import math
from functions import *

def transitive_closure(m):
    identity_matrix = construct_identity(len(m))

    mi = add(m, identity_matrix)

    res = deepcopy(mi)

    iteration = 1

    for n in range(len(m)):
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

