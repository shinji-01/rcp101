import string

def print_matrix(m):
    header = '  '.join(string.digits[i] for i in range(len(m)))
    print(f'\n   {header}')

    for i in range(len(m)):
        print(string.digits[i], end=' ')
        line = ', '.join(str(n) for n in m[i])

        print(f'({line})')


def multiply(m, m2):
    # Pour ne pas modifier la matrice originale
    m_len = len(m)
    res = deepcopy(m)

    # Double boucle pour mettre les valeurs de la nouvelle matrice
    for i in range(m_len):
        for j in range(m_len):
            val = 0

            for k in range(m_len):
                val += m[i][k] * m2[k][j]

            res[i][j] = val

    return res

# Remplace toutes les valeurs au-dessus de 1 par 1
def binarize(m):
    m_len = len(m)
    res = deepcopy(m)

    for i in range(m_len):
        for j in range(m_len):
            # Devient True ou False puis est converti en int avec "+ 0"
            res[i][j] = (res[i][j] >= 1) + 0

    return res


def add(m, m2):
    # Pour ne pas modifier la matrice originale
    m_len = len(m)
    res = deepcopy(m)

    # Double boucle pour mettre les valeurs de la nouvelle matrice
    for i in range(m_len):
        for j in range(m_len):
            res[i][j] = m[i][j] + m2[i][j]

    return res


def construct_identity(length):
    res = [[0 for x in range(length)] for y in range(length)] 

    for i in range(length):
        res[i][i] = 1

    return res

def has_changed(m, m2):
    for i in range(len(m)):
        for j in range(len(m)):
            if m[i][j] != m2[i][j]:
                return True

    return False

def get_edges(matrix):
    res = []

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] != 0:
                res.append(tuple((i, j)))

    return res

