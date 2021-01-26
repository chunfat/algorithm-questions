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

set1 = list()
set2 = list()
set3 = list()

n = inp()
for i, v in enumerate(inlt()):
    if v is 1:
        set1.append(i + 1)
    elif v is 2:
        set2.append(i + 1)
    else:
        set3.append(i + 1)

team_len = min(len(set1), len(set2), len(set3))

sys.stdout.write(str(team_len) + '\n')



if team_len > 0:
    for i in range(0, team_len):
        sys.stdout.write(str(set1[i]) + ' ')
        sys.stdout.write(str(set2[i]) + ' ')
        sys.stdout.write(str(set3[i]) + '\n')