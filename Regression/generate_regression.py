import numpy as np


def f1(x, a, b):
    return a*x+b

def f2(x, a, b, c, d):
    return a*x**3 + b*x**2 + c*x + d

def f3(x, a, b):
    return a*np.exp(b*x)

x = np.arange(-10, 10, 0.5)
n = 20*np.random.uniform(-10, 10, 40)

y1 = f1(x, 100, 0) + n
y2 = f2(x, 1, 2, 0, 0) + n
y3 = f3(x, 1, 0.75) + n


def generate(link, m, y):
    with open(link, "w") as f:
        f.write(m+"\n")
        for i in y:
            f.write(str(i)+"\n")

generate("regression_data1.txt", "l", y1)
generate("regression_data2.txt", "p", y2)
generate("regression_data3.txt", "e", y3)

