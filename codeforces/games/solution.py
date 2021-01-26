# 11:07
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

ans = 0

n = inp();
u = list([[0,0]])

while n > 0:
    u.append(inlt())
    n -= 1

for t1 in range(1, len(u)):
    for t2 in range(1, len(u)):
        if t1 is not t2:
            if u[t1][0] is u[t2][1]:
                ans += 1


sys.stdout.write(str(ans) + '\n')