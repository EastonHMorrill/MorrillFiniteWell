import numpy as np

def find_sign_changes(f, step, a, b):
    x = a
    pairs = []
    while (x + step < b):
        if (f(x + step)/f(x) < 0):
            pairs.append([x, x+step])
        x += step
    return pairs

def bisection(f, pairs, tolerance):
    zeroes = []
    for pair in pairs:
        midpoint = (pair[1] - pair[0])/2 + pair[0]
        while (abs(f(midpoint)) > tolerance):
            if (f(midpoint)/f(pair[0]) < 0):
                pair[1] = midpoint
            else:
                pair[0] = midpoint
            midpoint = (pair[1] - pair[0])/2 + pair[0]
        zeroes.append(midpoint)
    return zeroes

def sinc(x):
    if (x == 0):
        return 1
    else:
        return np.sin(x)/x

pairs = find_sign_changes(sinc, 0.1, 0, 10)
print(pairs)
zeroes = bisection(sinc, pairs, 1E-10)
print(zeroes)
print(np.pi, 2*np.pi, 3*np.pi)