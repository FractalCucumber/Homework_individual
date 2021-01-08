import random
import matplotlib.pyplot as plt

N = 10000
n = 500
r = 5


plt.subplot(2, 2, 1, title="dataset")
with open("clusterisation_dataset3.txt", "r") as f:
    dataset = []

    for line in f:
        line = line.split()
        xy = tuple(map(float, line))

        dataset += [xy]

plt.scatter([i[0] for i in dataset], [i[1] for i in dataset], s=0.5, c="blue")
train = random.sample(dataset, n)

dists = dict()

for i in train:
    for j in train:
        if i != j and (i, j) not in dists:
             dists[(i, j)] = (i[0] - j[0])**2 + (i[1] - j[1])**2

edges = sorted([i for i in dists.keys()], key=lambda j: dists[j])

clusters = dict()

for i in range(n):
    clusters[train[i]] = i
count_of_clusters = n

for _ in range(10):
    for i in edges:
        if dists[i] > r**2:
            break
        elif clusters[i[0]] != clusters[i[1]]:
            clusters[i[1]] = min(clusters[i[0]], clusters[i[1]])
            clusters[i[0]] = clusters[i[1]]
            count_of_clusters -= 1


rename = dict()
i = 0
for k in clusters:
    if clusters[k] in rename:
        clusters[k] = rename[clusters[k]]
    else:
        i += 1
        rename[clusters[k]] = i
        clusters[k] = rename[clusters[k]]


plt.subplot(2, 2, 2, title="hierarchy")

cl = dict()

for i in range(n):
    c = clusters[train[i]]
    x = train[i][0]
    y = train[i][1]
    if c in cl:
        cl[c] += [(x, y)]
    else:
        cl[c] = [(x, y)]

for c in cl:
    plt.scatter([i[0] for i in cl[c]], [i[1] for i in cl[c]], s=0.5)


for attempt in range(2):
    if not attempt == 0:
        for i in dataset:
            x = i[0]
            y = i[1]
            min_dist = 4*x**2 + 4*y**2
            for cls in means:
                x0 = means[cls][0]
                y0 = means[cls][1]

                if (x-x0)**2 + (y-y0)**2 < min_dist:
                    nearest_centre = (x0, y0)
                    min_dist = (x-x0)**2 + (y-y0)**2
                    cluster_i = cls

            clusters[i] = cluster_i

    means = dict()
    for i in clusters:
        cls = clusters[i]
        if cls not in means:
            means[cls] = [i[0], i[1], 1]
        else:
            means[cls][0] += i[0]  # х среднего
            means[cls][1] += i[1]  # у среднего
            means[cls][2] += 1  # кол-во точек в предварительном кластере
    for cls in means:
        means[cls][0] /= means[cls][2]
        means[cls][1] /= means[cls][2]



plt.subplot(2, 2, 4, title="k-means")

cl = dict()

for i in range(N):
    c = clusters[dataset[i]]
    x = dataset[i][0]
    y = dataset[i][1]
    if c in cl:
        cl[c] += [(x, y)]
    else:
        cl[c] = [(x, y)]

for c in cl:
    plt.scatter([i[0] for i in cl[c]], [i[1] for i in cl[c]], s=0.5)


plt.show()




