import sys

for line in sys.stdin:
    x1, y1, x2, y2, x3, y3, x4, y4 =  map(float, line.strip().split(" "))
    pts = []
    st = set()

    pts.append((x1, y1))
    pts.append((x2, y2))
    pts.append((x3, y3))
    pts.append((x4, y4))

    cx = 0
    cy = 0

    for pt in pts:
        if pt not in st:
            st.add(pt)
        else:
            st.remove(pt)
            cx = pt[0]
            cy = pt[1]

    lt = list(st)
    ax, ay = lt[0]
    bx, by = lt[1]

    sys.stdout.write("{:.3f}".format(ax + bx - cx) + ' ' + "{:.3f}".format(ay + by - cy) + '\n')