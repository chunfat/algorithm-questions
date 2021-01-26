import os
import sys
from atexit import register
from io import BytesIO

sys.stdin = BytesIO(os.read(0, os.fstat(0).st_size))
sys.stdout = BytesIO()
register(lambda: os.write(1, sys.stdout.getvalue()))

input = lambda: sys.stdin.readline().rstrip('\r\n')

# ref. https://codeforces.com/blog/entry/71884
def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s)]))
def invr():
    return(map(int,input().split()))

ans = 0

n = 5

while n > 0:
    row = inlt()
    for i, c in enumerate(row):
        if c == 1:
            # one found
            ans = abs(n - 3) + abs(i - 2)
    n -= 1


sys.stdout.write(str(ans) + '\n')