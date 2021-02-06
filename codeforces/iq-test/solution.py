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

directions = [(0, 0), (0, 1), (1, 0), (1, 1)]

def solve(picture):
    for r in range(0, len(picture) - 1):
        row = picture[r]
        for c in range(0, len(row) - 1):
            color1 = 0
            color2 = 0
            for dir in directions:
                dr, dc = dir
                if picture[r + dr][c + dc] == '#':
                    color1 += 1
                else:
                    color2 += 1
            if color1 >= 3 or color2 >= 3:
                return True
    return False

picture = []

for line in sys.stdin:
    picture.append([x for x in line.strip()])
    
if solve(picture):
    sys.stdout.write('YES\n')
else:
    sys.stdout.write('NO\n')
