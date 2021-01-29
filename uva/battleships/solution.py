import sys

def dfs(g, row, col):
    if g[row][col] == '.': return

    g[row][col] = '.'

    # up
    if row > 0:
        dfs(g, row - 1, col)
    
    # down
    if row < len(g) - 1:
        dfs(g, row + 1, col)
    
    # left
    if col > 0:
        dfs(g, row, col - 1)
    
    if col < len(g[row]) - 1:
        dfs(g, row, col + 1)


T = int(input())
case = 0

while case < T:
    case += 1

    N = int(input())
    g = list()

    while N > 0:
        g.append([c for c in input()])
        N -= 1

    ships = 0

    for i in range(0, len(g)):
        for j in range(0, len(g[i])):
            if g[i][j] == 'x':
                ships += 1
                dfs(g, i, j)

    sys.stdout.write('Case ' + str(case) + ': ' + str(ships) +'\n')

