n, m = map(int, input().split())

matrixA = []
for _ in range(n):
    row1 = list(map(int, input().split()))
    matrixA.append(row1)

zero_rows = []
zero_cols = []

for i in range(n):
    for j in range(m):
        if matrixA[i][j] == 0:
            zero_rows.append(i)
            zero_cols.append(j)

zero_rows = list(dict.fromkeys(zero_rows))
zero_cols = list(dict.fromkeys(zero_cols))

#print(zero_rows)
#print(zero_cols)

for r in zero_rows:
    for j in range(m):
        matrixA[r][j] = 0

for i in range(n):
    for c in zero_cols:
        matrixA[i][c] = 0

for i in matrixA:
    print(*i)
