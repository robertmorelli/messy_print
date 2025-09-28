from math import log10, floor
from itertools import accumulate
def print_num(N):
    def update(a, i):
        _, n = a
        if (i == floor(n)):
            g = floor(10.0 ** (n - floor(n)))
            return (chr(g + ord('0')), n + log10(1.0 - 10.0 ** (floor(n) - n) * g))
        else:
            return ('0', n)
    first = lambda a: a[0]
    log_N = log10(N)
    places = range(floor(log_N), -1, -1)
    print(''.join(map(first, accumulate(places, update, initial=('',log_N)))))
