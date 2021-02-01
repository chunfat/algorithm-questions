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

# must be an odd number as described
n = inp()

c = 0

seen = set()
x = ''

ans = True

while n > c:
    # check both x1 and x2 must be the same
    x1 = c
    x2 = abs(n - 1 - x1)

    # check other char must be different to x1
    # only 2 kinds of char allowed

    row = insr()

    for i in range(0, n):

        # inital the diagonal char
        if x == '':
            x = row[i]

        if i == x1 or i == x2:
            if row[i] != x: 
                ans = False
                break
        elif row[i] == x:
            ans = False
            break

        seen.add(row[i])

        if len(seen) > 2:
            ans = False
            break
    
    if ans == False:
        break
    
    c+=1

if ans == True:
    sys.stdout.write('YES\n')
else:
    sys.stdout.write('NO\n')