def dimensao_matriz(m):
    linhas = len(m)
    colunas = len(m[0])
    return linhas, colunas


def soma_matrizes(m1, m2):
    if dimensao_matriz(m1) == dimensao_matriz(m2):
        matriz = []
        for i, j in range(m1), range(m2):
            lista = []
            for x, y in i, j:
                valor = x + y
                lista.append(valor)
            matriz.append(lista)
        return matriz
    return False

m1 = [[1, 2, 3], [4, 5, 6]]
m2 = [[2, 3, 4], [5, 6, 7]]

print(soma_matrizes(m1, m2))