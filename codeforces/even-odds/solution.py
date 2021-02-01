import sys
import math

n, k = map(int, input().split(" "))

m = math.ceil(n / 2)

ans = 0

if k > m:
    # even
    ans = 2 * (k - m)
else:
    # odd
    ans = 2 * k - 1

sys.stdout.write(str(ans) + '\n')
