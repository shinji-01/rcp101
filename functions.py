import string

def format_path(path):
    letter_path = [string.ascii_uppercase[vertex] for vertex in path]
    return ' => '.join(letter_path)

def path_reconstruction(matrix, route):
    start = route[0]
    end = route[1]

    if matrix[start][end] == None:
        return []

    path = [start]

    while start != end:
        start = matrix[start][end]
        path.append(start)

    return path

def print_matrix(matrix):
    header = '  '.join(string.ascii_uppercase[i] for i in range(len(matrix)))
    print(f'\n   {header}')

    for i in range(len(matrix)):
        print(string.ascii_uppercase[i], end=' ')
        line = ', '.join(str(n) for n in matrix[i])

        print(f'({line})')


def multiply(matrix, matrix2):
    # Pour ne pas modifier la matrice originale
    m_len = len(matrix)
    res = deepcopy(matrix)

    # Double boucle pour mettre les valeurs de la nouvelle matrice
    for i in range(m_len):
        for j in range(m_len):
            val = 0

            for k in range(m_len):
                val += matrix[i][k] * matrix2[k][j]

            res[i][j] = val

    return res

# Remplace toutes les valeurs au-dessus de 1 par 1
def binarize(matrix):
    m_len = len(matrix)
    res = deepcopy(matrix)

    for i in range(m_len):
        for j in range(m_len):
            # Devient True ou False puis est converti en int avec "+ 0"
            res[i][j] = (res[i][j] >= 1) + 0

    return res


def add(matrix, matrix2):
    # Pour ne pas modifier la matrice originale
    m_len = len(matrix)
    res = deepcopy(matrix)

    # Double boucle pour mettre les valeurs de la nouvelle matrice
    for i in range(m_len):
        for j in range(m_len):
            res[i][j] = matrix[i][j] + matrix2[i][j]

    return res

def construct_identity(length):
    res = [[0 for x in range(length)] for y in range(length)]

    for i in range(length):
        res[i][i] = 1

    return res

def has_changed(matrix, matrix2):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] != matrix2[i][j]:
                return True

    return False

def get_edges(matrix):
    res = []

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] != 0:
                res.append(tuple((i, j)))

    return res

