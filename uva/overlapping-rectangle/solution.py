import sys

n = int(input())

def overlappingRegion(rect1, rect2):
    r1_ll_x, r1_ll_y = rect1[0]
    r1_ur_x, r1_ur_y = rect1[1]
    r2_ll_x, r2_ll_y = rect2[0]
    r2_ur_x, r2_ur_y = rect2[1]

    if max(r1_ll_x, r2_ll_x) < min(r1_ur_x, r2_ur_x) and max(r1_ll_y, r2_ll_y) < min(r1_ur_y, r2_ur_y):
        return [(max(r1_ll_x, r2_ll_x), max(r1_ll_y, r2_ll_y)), (min(r1_ur_x, r2_ur_x), min(r1_ur_y, r2_ur_y))]
    
    return []


while n > 0:
    line = input().strip()
    if line == '': continue

    x1, y1, x2, y2 = map(int, line.split(" "))
    x3, y3, x4, y4  = map(int, input().split(" "))

    rect1 = [(x1, y1), (x2, y2)]
    rect2 = [(x3, y3), (x4, y4)]

    result = overlappingRegion(rect1, rect2)

    if len(result) == 0:
        sys.stdout.write('No Overlap\n\n')
    else:
        sys.stdout.write(" ".join([str(r[0]) + ' ' + str(r[1]) for r in result]) + '\n\n')

    n-=1
