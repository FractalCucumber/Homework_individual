import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import cKDTree, Voronoi, voronoi_plot_2d


with open("data.txt", "r") as f:
    a = list(map(int, f.readline().split())) # вертикальные улицы
    b = list(map(int, f.readline().split())) # горизонтальные улицы
    k1 = len(a)
    k2 = len(b)
    a.sort()
    b.sort()

    l, n = map(int, f.readline().split()) # кол-во школ и домов

    sch = []
    h = []

    for _ in range(l):
        sch += [list(map(int, f.readline().split()))] # (x, y) школы
    for _ in range(n):
        h += [list(map(int, f.readline().split()))] # (x, y) дома


kdtree = cKDTree(np.array(sch))
h_regions = kdtree.query(np.array(h))[1]

for i in range(n):
    print("Дом:", h[i], "Ближайшая школа:", sch[h_regions[i]])



vor = Voronoi(np.array(sch))

fig = voronoi_plot_2d(vor, show_vertices=False, line_colors='blue')
plt.vlines(np.array(a), 0, 1000, "lightgray")
plt.hlines(np.array(b), 0, 1000, "lightgray")
plt.plot(np.array([i[0] for i in h]), np.array([i[1] for i in h]), "r.")
plt.show()

