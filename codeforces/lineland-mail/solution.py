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
c = inlt()

for i in range(n):
    min_cost = sys.maxint
    max_cost = -sys.maxint - 1

    if i == 0:
        min_cost = abs(c[i + 1] - c[i])
        max_cost = abs(c[n - 1] - c[i])
    elif i == n - 1:
        min_cost = abs(c[i] - c[i - 1])
        max_cost = abs(c[i] - c[0])
    else:
        # min cost is the min of adjacent val
        min_cost = min(abs(c[i] - c[i - 1]), abs(c[i + 1] - c[i]))
        # max cost is the fartest one
        max_cost = max(abs(c[n - 1] - c[i]), abs(c[i] - c[0]))
    sys.stdout.write(str(min_cost) + ' ' + str(max_cost) + '\n')


