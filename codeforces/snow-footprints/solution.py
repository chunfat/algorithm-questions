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
fps = input().strip()

left = []
right = []
for i, fp in enumerate(fps):
    if fp == '.': continue
    if fp == 'L': left.append(i + 1)
    else: right.append(i + 1)

if len(right) == 0:
    # only has L
    sys.stdout.write(str(left[-1]) + ' ' + str(left[0] - 1) + '\n')
elif len(left) == 0:
    sys.stdout.write(str(right[0]) + ' ' + str(right[-1] + 1) + '\n')
else:
    s = min(right)
    t = min(left)
    sys.stdout.write(str(s) + ' ' + str(t) + '\n')
