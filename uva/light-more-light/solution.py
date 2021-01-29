import sys
import math

c = 0

# Keys:
# 1. A corridor with N bulbs
# 2. Toggle bulb 1 to N times
# 3. At i-th toggle, only toggle bulbs that divisble by i
# 4. Return the state of N-th bulb after toggle N times. 

# Idea:
# 1. After toggled N times, the N-th bulb would be toggled on Z times
# 2. Z is the number of positive factor of N.
# 3. If Z is odd => On, else => Off
# e.g. N = 8, after 8 visits, 8th bulb would be toggled 4 times
#       At 1-th visit, 8th bulb toggled on
#       At 2-th visit, 8th bulb toggled off
#       At 4-th visit, 8th bulb toggled on
#       At 8-th visit, 8th bulb toggled off
#      They are the positive factors of 8.
# 
# Similarly, 
# N =  9, positive factors are 1, 3, 9 => On
# N = 12, positive factors are 1, 2, 3, 4, 6, 12 => Off
# N = 13, positive factors are 1, 13 => On
# N = 16, positive factors are 1, 2, 4, 8, 16 => Off
#
# Based on the above observations, 
# if N is a perfect square, the N-th bulb state would be On

while True:
    N = int(input())
    
    # end of process
    if N is 0: break

    root = math.sqrt(N)
    
    # check if it is a perfect square
    if root - math.floor(root) == 0:
        sys.stdout.write('yes\n')
    else:
        sys.stdout.write('no\n')
    