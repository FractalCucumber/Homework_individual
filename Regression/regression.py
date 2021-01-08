import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


x = np.arange(-10, 10, 0.5)


def f1(x, n, *args):
    res = 0
    for i in range(n+1):
        res += args[i]*x**(n-i)
    return res


def f2(x, a, b):
    return a*np.exp(b*x)

link = "regression_data1.txt"

y = []
with open(link) as f:
    m = f.readline().rstrip()
    if m == "p":
        n = int(f.readline())
    elif m == "l":
        n = 1
    elif m == "e":
        n = -1
    while True:
        line = f.readline()
        if not line:
            break
        y += [float(line)]

y = np.array(y)


if m == "l" or m == "p":
    f = f1
elif m == "e":
    f = f2

if m == "p" or m == "l":
    p = np.polyfit(x, y, n)
elif m == "e":
    p = curve_fit(f, x, y)[0]

print(p)

if m == "p" or m == "l":
    plt.plot(x, y, ".", x, f(x, n, *p))
else:
    plt.plot(x, y, ".", x, f(x, *p))

plt.show()