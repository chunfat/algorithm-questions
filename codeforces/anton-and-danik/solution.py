# https://codeforces.com/contest/734/problem/A

import os
import sys
from atexit import register
from io import BytesIO

sys.stdin = BytesIO(os.read(0, os.fstat(0).st_size))
sys.stdout = BytesIO()
register(lambda: os.write(1, sys.stdout.getvalue()))

input = lambda: sys.stdin.readline().rstrip('\r\n')

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
games = insr()

a_won = 0
d_won = 0

for game in games:
    if game == 'A':
        a_won += 1
    else:
        d_won += 1

if a_won > d_won:
    sys.stdout.write(str('Anton') + "\n")
elif a_won < d_won:
    sys.stdout.write(str('Danik') + "\n")
else:
    sys.stdout.write(str('Friendship') + "\n")
