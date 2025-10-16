n, m = map(int, input().split())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))
# for row in matrix:
# print(row)

damage = [[0] * m for _ in range(n)]
damage[0][0] = matrix[0][0]
for i in range(1, n):
    damage[i][0] = damage[i - 1][0] + matrix[i][0]
for j in range(1, m):
    damage[0][j] = damage[0][j - 1] + matrix[0][j]

for i in range(1, n):
    for j in range(1, m):
        damage[i][j] = min(damage[i - 1][j], damage[i][j - 1]) + matrix[i][j]

print(damage[n - 1][m - 1])
