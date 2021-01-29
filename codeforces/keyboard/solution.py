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

keyboard = list(["qwertyuiop", "asdfghjkl;", "zxcvbnm,./"])

keyboardMap = {
    'q': [0, 0],
    'w': [0, 1],
    'e': [0, 2],
    'r': [0, 3],
    't': [0, 4],
    'y': [0, 5],
    'u': [0, 6],
    'i': [0, 7],
    'o': [0, 8],
    'p': [0, 9],
    'a': [1, 0],
    's': [1, 1],
    'd': [1, 2],
    'f': [1, 3],
    'g': [1, 4],
    'h': [1, 5],
    'j': [1, 6],
    'k': [1, 7],
    'l': [1, 8],
    ';': [1, 9],
    'z': [2, 0],
    'x': [2, 1],
    'c': [2, 2],
    'v': [2, 3],
    'b': [2, 4],
    'n': [2, 5],
    'm': [2, 6],
    ',': [2, 7],
    '.': [2, 8],
    '/': [2, 9],
}

shift = -1 if input() == 'R' else 1
word = insr()

ans = ''

for c in word:
    row, col = keyboardMap[c]
    ans += keyboard[row][col + shift]


sys.stdout.write(ans + '\n')
