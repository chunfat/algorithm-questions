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

n, t, k, d = inlt()

# total baking required for 1 oven
m = n/k
# add one more if n is not divisble by k
if n % k != 0:
    m += 1
# total time required for n cakes
x = m * t

# if the built time + bake time of 2nd oven
# take less than x, 
# means adding 2nd oven would increase bake speed
if d + t < x:
    sys.stdout.write('YES\n')
else:
    sys.stdout.write('NO\n')