import random
import math

n = 10000

with open("clusterisation_dataset1.txt", "w") as f:

    for _ in range(n):

        R1 = 5**2
        R2 = 10**2
        R3 = 20**2
        R4 = 35**2
        R5 = 40**2
        R6 = 50**2

        r = 0

        while not ((r >= R1 and r <= R2) or (r >= R3 and r <= R4) or (r >= R5 and r <= R6)):
            x = round(random.uniform(1, 100), 3)
            y = round(random.uniform(1, 100), 3)

            r = (x-50)**2 + (y-50)**2

        f.write(str(x) + " " + str(y) + "\n")


with open("clusterisation_dataset2.txt", "w") as f:
    for _ in range(n):
        R1 = 20**2
        R2 = 10**2
        R3 = 25**2

        r1=-1
        r2=-1
        r3=-1

        while not ((r1 >= 0 and r1 <= R1) or (r2 >= R2 and r2 <= R3) or (r3 >= 0 and r3 <= R2)):
            x = round(random.uniform(1, 100), 3)
            y = round(random.uniform(1, 100), 3)

            r1 = (x-25)**2 + (y-40)**2
            r2 = (x-70)**2 + (y-60)**2
            r3 = (x-60)**2 + (y-20)**2

        f.write(str(x) + " " + str(y) + "\n")


with open("clusterisation_dataset3.txt", "w") as f:
    for _ in range(n//2):

        x = round(random.uniform(1, 100), 3)
        y1 = 2*math.sin(x) + round(random.uniform(0, 1), 3)
        y2 = 10 + 0.1*abs(x*math.sin(x)) + round(random.uniform(0, 1), 3)

        f.write(str(x) + " " + str(y1) + "\n")
        f.write(str(x) + " " + str(y2) + "\n")
