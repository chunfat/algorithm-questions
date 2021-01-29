# 4:30
import sys

stones = "IEHOVA#"

def move(g, row, col, t, path):
    if t == len(stones): return

    if row > 0 and g[row - 1][col] == stones[t]:
        path.append('forth')
        move(g, row - 1, col, t + 1, path)
    elif col > 0 and g[row][col - 1] == stones[t]:
        path.append('left')
        move(g, row, col - 1, t + 1, path)
    elif col < len(g[row]) and g[row][col + 1] == stones[t]:
        path.append('right')
        move(g, row, col + 1, t + 1, path)

c = int(input())

while c > 0:
    n, m = map(int, input().rstrip('\r\n').split(" "))
    
    g = list()

    start_row = n - 1
    start_col = 0
    r = 0
    while r < n:
        row = list()
        for i, char in enumerate(input()):
            row.append(char)
            if char == '@':
                start_col = i

        g.append(row)
        r += 1

    path = []
    move(g, start_row, start_col, 0, path)

    sys.stdout.write(" ".join(path) + '\n')

    c-=1
    