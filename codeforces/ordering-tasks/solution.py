# 10: 56

import sys

def topological_sort(g, n, path, visited):
    if n in visited: return

    visited.add(n)

    for node in g[n]:
        topological_sort(g, node, path, visited)
    
    path.append(n)


for line in sys.stdin:
    n, m = map(int, line.rstrip('\r\n').split(" "))
    if n == 0 and m == 0: break;

    adj_list = [list() for i in range(n + 1)]
    c = 1
    while c <= m:
        i, j = map(int, input().rstrip('\r\n').split(" "))
        adj_list[i].append(j)
        c += 1

    path = []
    visited = set()
    for node in range(1, len(adj_list)):
        topological_sort(adj_list, node, path, visited)

    sys.stdout.write(" ".join([str(n) for n in reversed(path)]) + "\n")

