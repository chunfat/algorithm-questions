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

s = input().strip()
s_len = len(s)

ans = 0

if s_len & 1 == 1:
    # odd length
    more_one = False

    for i in range(1, s_len):
        if s[i] == '1':
            more_one = True
            break
    
    if more_one is True:
        ans = s_len / 2 + 1
    else:
        ans = s_len / 2

else:
    # even length
    ans = s_len / 2

sys.stdout.write(str(ans) + '\n')
