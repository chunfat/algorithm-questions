import sys

def isLeafYear(year):
    if year % 4 == 0 and year % 100 != 0:
        return True
    if year % 400 == 0:
        return True
    return False

def nextDayOf(d, m, y):
    dayOfMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    dayofMonth = dayOfMonths[m - 1]

    # February and is leaf year
    if m is 2:
        if isLeafYear(y):
            dayofMonth = dayofMonth + 1

    if d < dayofMonth:
        d += 1
    else:
        d = 1
        m += 1
    
    if m > 12:
        m = 1
        y += 1
    return d, m, y
        
records = list()

for line in sys.stdin:
    n = int(line.rstrip('\r\n'))
    if n == 0: break
    while n > 0:
        records.append(list(map(int, input().rstrip('\r\n').split(" "))))
        n-=1

    days = 0
    consumption = 0

    for i in range(0, len(records) - 1):
        curr_D, curr_M, curr_Y, curr_C = records[i]
        next_D, next_M, next_Y, next_C = records[i + 1]
        expt_D, expt_M, expt_Y = nextDayOf(curr_D, curr_M, curr_Y)

        if expt_D == next_D and expt_M == next_M and expt_Y == next_Y:
            days += 1
            consumption += next_C - curr_C
    
    sys.stdout.write(str(days) + ' ' + str(consumption) + '\n')

    records = list()