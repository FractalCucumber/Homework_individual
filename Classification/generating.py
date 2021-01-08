import random

with open("data.txt", "w") as f:

    a = [random.randint(0, 100)]
    while a[-1] < 931:
        a += [a[-1]+random.randint(20, 70)]
    b = [random.randint(0, 100)]
    while b[-1] < 931:
        b += [b[-1]+random.randint(20, 70)]

    f.write(" ".join(map(str, a))+"\n")
    f.write(" ".join(map(str, b))+"\n")

    l = 20
    n = 50

    f.write(str(l)+" "+str(n)+"\n")

    for _ in range(l):
        x = random.randint(0, 1000)
        y = random.randint(0, 1000)
        f.write(str(x)+" "+str(y)+"\n")
    for _ in range(n):
        x = random.randint(0, 1000)
        y = random.randint(0, 1000)
        f.write(str(x)+" "+str(y)+"\n")





