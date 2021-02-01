import sys

def topological_sort(g, n, visited, path):
    if n in visited: return

    visited.add(n)

    # in graph
    if n < len(g):
        # go thru each neighbors
        for i in g[n]:
            topological_sort(g, i, visited, path)

    # push current node to path
    path.append(n)

N, K = map(int, input().split(" "))

i = 0
adj_list = [[0]]

while i < K:
    l = list(map(int, input().split(" ")))
    l.pop(0)
    adj_list.append(l)
    i+=1

visited = set()
path = []
for i in range(1, N + 1):
    topological_sort(adj_list, i, visited, path)

parents = [-1] * (N + 1)
position = 0

for i in reversed(range(len(path))):
    node = path[i]
    parents[node] = position
    position = node

for i in range(1, len(parents)):
    sys.stdout.write(str(parents[i]) + '\n')