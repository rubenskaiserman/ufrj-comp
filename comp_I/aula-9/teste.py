def transposta(matriz):
    nlin = len(matriz)
    ncol = len(matriz[0])

    ret = []
    for i in range(nlin):
        for j in range(ncol):
            ret[i][j] = matriz[j][i]
    return ret

res =transposta([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
for line in res:
    print(line)