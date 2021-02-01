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

def isPrime(num):

    # if 2...num has divisor of num
    # only need to check up to sqrt(num)

    n = int(math.sqrt(num))

    for i in range(2, n + 1):
        if num % i == 0:
            # divsor found
            return False

    return True

n, m = inlt()

if isPrime(m) == False:
    sys.stdout.write('NO\n')
else:
    ans = 'YES'

    for i in range(n + 1, m):
        if isPrime(i) == True:
            ans = 'NO'
            break

    sys.stdout.write(ans + '\n')