# 2:58
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

y, w = inlt()

denominator = 6
numerator = 7 - max(y, w)

if numerator is 0:
    sys.stdout.write('0/1\n')
elif numerator is 6:
    sys.stdout.write('1/1\n')
elif numerator is 2:
    sys.stdout.write('1/3\n')
elif numerator is 3:
    sys.stdout.write('1/2\n')
elif numerator is 4:
    sys.stdout.write('2/3\n')
else:
    sys.stdout.write(str(numerator) + '/' + str(denominator) + '\n')


