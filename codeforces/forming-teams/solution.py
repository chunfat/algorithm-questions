import os
import sys
from atexit import register
from io import BytesIO

sys.stdin = BytesIO(os.read(0, os.fstat(0).st_size))
sys.stdout = BytesIO()
register(lambda: os.write(1, sys.stdout.getvalue()))

input = lambda: sys.stdin.readline().rstrip('\r\n')

n, m = map(int, input().split())

c = 0

g = {}

#  initiate graph
while c < m:
    a, b = map(int, input().split())
    if a not in g: g[a] = []
    if b not in g: g[b] = []
    g[a].append(b)
    g[b].append(a)
    c += 1

# try to color the graph
colors = [0] * (n + 1)
ans = 0
stack = []

for i in range(1, n + 1):
    if colors[i] != 0: continue
    colors[i] = 1
    stack.append(i)
    while len(stack) > 0:
        node = stack.pop()
        fillColor = 1 if colors[node] == 2 else 2
        if node not in g: continue
        for e in g[node]:
            if colors[e] == 0:
                colors[e] = fillColor
                stack.append(e)
            elif colors[e] != fillColor:
                ans+=1

# divide it by 2 since archenemies would be in pairs
ans = int(ans/2)

# make sure team size is equal
if (n - ans) % 2 is 1: ans+=1

sys.stdout.write(str(ans) + '\n')