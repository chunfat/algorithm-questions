# 7:17
import os
import sys
from atexit import register
from io import BytesIO
import random

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

n, k = inlt()

c = k
used = set()
ans = ''

while c > 0:
    letter = chr(random.randint(ord('a'), ord('z')))
    while letter in used:
        letter = chr(random.randint(ord('a'), ord('z')))
    used.add(letter)
    c -= 1

dict = list(used)

ans = "".join(dict)

c = k

while n > c:
    letter = dict[random.randint(0, k - 1)]
    while ans[len(ans) - 1] == letter:
        letter = dict[random.randint(0, k - 1)]
    ans += letter
    c += 1

sys.stdout.write(str(ans) + '\n')