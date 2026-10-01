def matrixmul(a:list[list[int|float]], b:list[list[int|float]])-> list[list[int|float]]:
    row_a, col_a = len(a), len(a[0])
    row_b, col_b = len(b), len(b[0])
    if col_a != row_b:
        return -1
    result = []
    for i in range(row_a):
        rows = []
        for z in range(col_b):
            temp = 0
            for j in range(col_a):
                temp += a[i][j] * b[j][z]
            rows.append(temp)
        result.append(rows)
    return result