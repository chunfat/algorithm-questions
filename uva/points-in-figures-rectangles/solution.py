import math
import sys

def inRectangle(rect, x, y):
    upper_x, upper_y = rect[0]
    lower_x, lower_y = rect[1]
    # print(upper_x, "<", x, '<', lower_x, upper_x < x and x < lower_x)
    # print(lower_y, "<", y, '<', upper_y, lower_y < y and y < upper_y)
    if upper_x < x and x < lower_x and lower_y < y and y < upper_y:
        return True

    return False

# rectangles
rectangles = []
for line in sys.stdin:
    line = line.strip()
    if line == '*': break
    line = line.split()
    line.pop(0)
    x1, y1, x2, y2 = map(float, line)
    rectangles.append([(x1, y1), (x2, y2)])

pt_c = 0
# points in rectangles
for line in sys.stdin:
    pt_c += 1
    line = line.strip()
    x, y = map(float, line.split())
    if x == 9999.9 and y == 9999.9: break
    found = False
    # check in pt in rect
    for i, rect in enumerate(rectangles):
        if inRectangle(rect, x, y):
            sys.stdout.write('Point ' + str(pt_c) + ' is contained in figure ' + str(i + 1) + '\n')
            found = True
    if not found:
        sys.stdout.write('Point ' + str(pt_c) + ' is not contained in any figure\n')
