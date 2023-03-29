import sys
n, k = map(int, sys.stdin.readline().split())
weight_list =[]
for _ in range(n):
    weight_list.append(list(map(int, sys.stdin.readline().split())))

dp = [[0 for _ in range(k+1)] for _ in range(n)]

for i in range(k+1):
    w0, v0 = weight_list[0]
    dp[0][i] = 0 if i < w0 else v0

for i in range(1, n):
    wi, vi = weight_list[i]
    for j in range(k+1):
        dp[i][j] = dp[i-1][j] if j < wi else max(vi + dp[i-1][j-wi], dp[i-1][j])

print(dp[n-1][k])
