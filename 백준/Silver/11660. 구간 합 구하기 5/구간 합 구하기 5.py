import sys
n, m = list(map(int, sys.stdin.readline().split()))

matrix = []
for _ in range(n):
    matrix.append(list(map(int, sys.stdin.readline().split())))

l = len(matrix[0])

matsum = [[0]*(l+1)]
for i in range(n):
    subsum = [0]
    for j in range(l):
        subsum.append(subsum[-1] + matrix[i][j])
    subsum = [subsum[k] + matsum[i][k] for k in range(l+1)]
    matsum.append(subsum)

answer_list = []
for _ in range(m):
    x1, y1, x2, y2 = list(map(int, sys.stdin.readline().split()))
    answer = matsum[x2][y2] - matsum[x2][y1-1] - matsum[x1-1][y2] + matsum[x1-1][y1-1]
    answer_list.append(answer)

for ans in answer_list:
    print(ans)