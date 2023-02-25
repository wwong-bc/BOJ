import sys
n, m = list(map(int, sys.stdin.readline().split()))

graph = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = list(map(int, sys.stdin.readline().split()))
    graph[x].append(y)
    graph[y].append(x)

# 특정 노드의 케빈 베이컨 수 구하는 함수
def KevinBacon(node):
    current_visit = graph[node]
    next_visit = []
    dist = 1
    kbn_list = [0]  + [-1] * n
    while True:
        for current_node in current_visit:
            if kbn_list[current_node] != -1:
                continue
            kbn_list[current_node] = dist
            next_visit += graph[current_node]
        if not next_visit:
            return sum(kbn_list)
        dist += 1
        current_visit = next_visit
        next_visit = []

min_kbn = 987654321
min_index = -1
for i in range(1, n+1):
    #케빈 베이컨 수
    kbn = KevinBacon(i)
    if kbn < min_kbn:
        min_index = i
        min_kbn = kbn

print(min_index)
