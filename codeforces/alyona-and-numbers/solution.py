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

n, m = inlt()

freq_n = [0] * 5
freq_m = [0] * 5

for i in range(1, n + 1):
    freq_n[i % 5] += 1

for i in range(1, m + 1):
    freq_m[i % 5] += 1

ans = freq_n[0] * freq_m[0] + freq_n[1] * freq_m[4] + freq_n[2] * freq_m[3] + freq_n[3] * freq_m[2] + freq_n[4] * freq_m[1]

sys.stdout.write(str(ans) + '\n')
