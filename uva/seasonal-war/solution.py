import sys

def dfs(image, row, col):
    if image[row][col] == 0: return

    # update the current cell to 0, avoid duplication
    image[row][col] = 0

    # dive into all directions

    # up
    if row > 0: 
        dfs(image, row - 1, col)
    # down
    if row < len(image) - 1: 
        dfs(image, row + 1, col)

    # left
    if col > 0: 
        dfs(image, row, col - 1)
    # right
    if col < len(image[row]) - 1: 
        dfs(image, row, col + 1)

    # up left
    if row > 0 and col > 0:
        dfs(image, row - 1, col - 1)

    # up right
    if row > 0 and col < len(image[row]) - 1:
        dfs(image, row - 1, col + 1)

    # down left
    if row < len(image) - 1 and col > 0: 
        dfs(image, row + 1, col - 1)

    # down right
    if row < len(image) - 1 and col < len(image[row]) - 1: 
        dfs(image, row + 1, col + 1)


c = 0

for line in sys.stdin:
    n = int(line.rstrip('\r\n'))
    image = list()

    while n > 0:
        image.append([int(c) for c in input()])
        n-=1
    
    ans = 0
    
    for i in range(0, len(image)):
        for j in range(0, len(image[i])):
            if image[i][j] == 1:
                ans += 1
                dfs(image, i, j)
    
    c += 1

    sys.stdout.write('Image number ' + str(c) +  ' contains ' + str(ans) + ' war eagles.\n')


