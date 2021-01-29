import sys
import math

for line in sys.stdin:
    n, m, c = map(int, line.rstrip('\r\n').split())

    if n == 0 and m == 0 and c == 0: break
    
    ans = ((n - 7) * (m - 7)) / 2

    ans = int(ans) if c == 0 else math.ceil(ans)

    sys.stdout.write(str(ans) + '\n')
