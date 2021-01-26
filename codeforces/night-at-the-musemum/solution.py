# 7:46
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

name = insr()
ans = 0
last = 'a'

# for i in name:
#     # compare clockwise to counter-clockwise
#     dist1 = 26 - (ord(last) - ord('a')) + ord(i)
#     dist2 = abs((ord(i) - ord(last)))
#     clockwise = min(dist1, dist2)

#     counterclockwise = 26 - clockwise

#     ans += min(clockwise, counterclockwise)

#     last = i

strt = 0

for i in name:
    index = ord(i) - 97
    dist = abs(strt - index)
    ans += dist if dist < 13 else 26 - dist
    strt = index

sys.stdout.write(str(ans) + '\n')