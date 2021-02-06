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

# 4*4
lock = [[0,0], [0,0]]

r1, r2 = inlt()
c1, c2 = inlt()
d1, d2 = inlt()

used = set()
g = 1
found = False
while g <= 9:
    used = set([g])
    
    lock[0][0] = g
    g += 1
    
    tmp = r1 - lock[0][0]
    if 0 < tmp and tmp <= 9 and tmp not in used:
        used.add(tmp)
        lock[0][1] = tmp
    else: continue

    tmp = c1 - lock[0][0]
    if 0 < tmp and tmp <= 9 and tmp not in used:
        used.add(tmp)
        lock[1][0] = tmp
    else: continue

    tmp = d1 - lock[0][0]
    if 0 < tmp and tmp <= 9 and tmp not in used:
        used.add(tmp)
        lock[1][1] = tmp
    else: continue

    if lock[1][0] + lock[1][1] == r2 and lock[1][0] + lock[0][1] == d2:
        found = True
        break

    used = set()

if found:
    for l in lock:
        sys.stdout.write(" ".join([str(g) for g in l]) + '\n')
else:
    sys.stdout.write("-1\n")