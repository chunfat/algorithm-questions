# https://codeforces.com/contest/791/problem/A

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

limak, bob = inlt()

year = 0

while limak <= bob:
    limak = limak * 3
    bob = bob * 2
    year = year + 1

sys.stdout.write(str(year) + "\n")
