import os
import sys
import math
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

def twoPointDistance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2

    return math.sqrt((math.pow(x2-x1, 2) + math.pow(y2 - y1, 2)))


n, k = inlt()

dist = 0

points = list()

while n > 0:
    x, y = map(float,input().split())
    points.append((x, y))
    n-=1

for i in range(1, len(points)):
    point1 = points[i - 1]
    point2 = points[i]
    dist += twoPointDistance(point1, point2)

wasted = dist/50 * k

sys.stdout.write("{:.9f}".format(wasted) + '\n')