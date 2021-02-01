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



def findTreeCenter(g):
    N = len(g)

    degree = [0] * N
    
    leaves = []

    # find all nodes' degree
    for i in range(1, N):
        degree[i] = len(g[i])
        if degree[i] == 0 or degree[i] == 1:
            leaves.append(i)

    visited = set()
    n = len(leaves)

    while n < N - 1:
        new_leaves = []
        for i in leaves:
            for j in g[i]:
                degree[j] -= 1
                if degree[j] == 1:
                    new_leaves.append(j)
            degree[i] = 0
        n += len(leaves)
        leaves = new_leaves

    return leaves

def rootTree():
    return

N, K = map(int, input().split(" "))

i = 0
adj_list = [ list() for i in range(N + 1)]

while i < K:
    l = list(map(int, input().split(" ")))
    l.pop(0)
    for j in l:
        adj_list[i + 1].append(j)
        adj_list[j].append(i + 1)

    i+=1
print(adj_list)
centers = findTreeCenter(adj_list)
print(centers)