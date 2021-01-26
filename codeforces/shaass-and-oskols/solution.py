# 3:39
import os
import sys
from atexit import register
from io import BytesIO

sys.stdin = BytesIO(os.read(0, os.fstat(0).st_size))
sys.stdout = BytesIO()
register(lambda: os.write(1, sys.stdout.getvalue()))

input = lambda: sys.stdin.readline().rstrip('\r\n')

# ref. https://codeforces.com/blog/entry/71884
# 1) inp(), For taking integer inputs.
# 2) inlt(), For taking List inputs.
# 3) insr(), For taking string inputs. 
#           Actually it returns a List of Characters, 
#           instead of a string, which is easier to use in Python, 
#           because in Python, Strings are Immutable.
# 4) invr(), For taking space seperated integer variable inputs.

def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s)]))
def invr():
    return(map(int,input().split()))

n = inp()
a = inlt()
m = inp()

while m > 0:
    x, y = inlt()

    i = x - 1 # i-th wire, 1-based
    left = y - 1 # no of left birds
    right = a[i] - y # no of right birds
    upper_wire = i - 1
    down_wire = i + 1

    a[i] = 0

    if upper_wire >= 0:
        a[upper_wire] += left

    if down_wire < n:
        a[down_wire] += right

    m -= 1


for i in a:
    sys.stdout.write(str(i) + '\n')