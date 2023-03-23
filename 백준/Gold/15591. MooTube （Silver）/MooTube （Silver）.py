import sys
n, q = map(int, sys.stdin.readline().split())

wgraph = {}
for _ in range(n-1):
    pi, qi, ri = map(int, sys.stdin.readline().split())
    if pi not in wgraph:
        wgraph[pi] = {}
    if qi not in wgraph:
        wgraph[qi] = {}
    wgraph[pi][qi] = ri
    wgraph[qi][pi] = ri

def usado(node):
    visited = [False] * (n + 1)
    usado_list = [-1] * (n + 1) 
    to_visit = [[node, next] for next in list(wgraph[node].keys())]
    visited[node] = True
    usado_list[node] = 0
    while to_visit:
        current_node, next_node = to_visit.pop(0)
        if usado_list[current_node] == 0:
            usado_list[next_node] = wgraph[current_node][next_node]
        else:
            usado_list[next_node] = min(wgraph[current_node][next_node], usado_list[current_node])
        visited[next_node] = True
        next_visit = list(wgraph[next_node])
        for nv in next_visit:
            if not visited[nv]:
                to_visit.append([next_node, nv])
    return usado_list

answer_list = []
for _ in range(q):
    k, v = map(int, sys.stdin.readline().split())
    answer = 0
    usado_list = usado(v)
    for u in usado_list:
        if u >= k:
            answer += 1
    answer_list.append(answer)

for ans in answer_list:
    print(ans)