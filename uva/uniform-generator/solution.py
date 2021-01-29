import sys

for line in sys.stdin:
    step, mod = line.rstrip('\r\n').split()
    step = int(step)
    mod = int(mod)
    last = 0
    seen = set()
    bad = False
    for i in range(0, mod):
        seed = (last + step) % mod
        if (seed in seen):
            bad = True
            break
        seen.add(seed)
        last = seed

    output = str(step).rjust(10) + str(mod).rjust(10) + ' ' * 4
    output += 'Good Choice\n' if not bad else 'Bad Choice\n'
    sys.stdout.write(output + '\n')

