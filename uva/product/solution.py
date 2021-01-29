import sys

def bigIntProduct(X, Y):
    X.reverse(), Y.reverse()
    cache = [0] * 600

    # fill the cache
    for i, v1 in enumerate(X):
        for j, v2 in enumerate(Y):
            cache[i + j] += int(v1) * int(v2)

    # process cache
    # eliminate zero
    for i, v in enumerate(cache):
        if i == len(cache) - 1: break
        cache[i + 1] += int(v / 10)
        cache[i] = v % 10

    c = len(cache) - 1
    while c > 0 and cache[c] == 0: c-=1;

    ans = [str(cache[i]) for i in range(0, c + 1)]
    ans.reverse()

    return "".join(ans)

c = 0
x = 0
y = 0

for line in sys.stdin:
    if c % 2 == 0:
        x = line.rstrip('\r\n')
    else:
        y = line.rstrip('\r\n')
        ans = bigIntProduct(list(x[:len(x)]), list(y[:len(y)]))
        sys.stdout.write(ans + '\n')
    c+=1