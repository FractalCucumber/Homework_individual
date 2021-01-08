from random import choice


m = int(input())
n = int(input())

A = [choice(("A", "C", "T", "G")) for i in range(m)]
B = [choice(("A", "C", "T", "G")) for j in range(n)]


v = [[0 for j in range(n)] for i in range(m)]  # v[i][j] - длина максимальной подпоследовательности для задачи P(i, j)


seq = [[]]  # массив для хранения индексов совпавших символов


if A[0] == B[0]:
    v[0][0] = 1
    seq[0] += [(0, 0)]
else:
    v[0][0] = 0

for k in range(1, m):
    if (v[k-1][0] == 1) or (A[k] == B[0]):
        v[k][0] = 1
        if (A[k] == B[0]) and not (v[k-1][0] == 1):
            seq[0] += [(k, 0)]
    else:
        v[k][0] = 0

for l in range(1, n):
    if (v[0][l-1] == 1) or (B[l] == A[0]):
        v[0][l] = 1
        if (B[l] == A[0]) and not (v[0][l-1] == 1):
            seq[0] += [(0, l)]
    else:
        v[0][l] = 0

for k in range(1, m):
    for l in range(1, n):
        if A[k] == B[l] and v[k-1][l-1] + 1 >= max(v[k-1][l-1], v[k][l-1]):
            v[k][l] = v[k-1][l-1] + 1
            if v[k-1][l] < v[k][l] and v[k][l-1] < v[k][l]:
                if len(seq) >= v[k][l]:
                    seq[v[k][l]-1] += [(k, l)]
                else:
                    seq += [[(k, l)]]
        else:
            v[k][l] = max(v[k-1][l], v[k][l-1])


seq = seq[::-1]
d = []
d += [seq[0][-1]]

# выбираем из совпавших сиволов такие, чтобы они образовывали подпоследовательность
for i in seq[1:]:
    for j in i:
        if j[0] < d[-1][0] and j[1] < d[-1][1]:
            d += [j]
d = d[::-1]

C = ""  # выровненная последовательность
A1 = ""
B1 = ""

for i in range(d[0][0]):
    C += A[i]
    A1 += A[i]
    B1 += "*"
for j in range(d[0][1]):
    C += B[j]
    B1 += B[j]
    A1 += "*"

C += A[d[0][0]]
A1 += A[d[0][0]]
B1 += A[d[0][0]]

for k in range(1, len(d)):
    for i in range(d[k-1][0]+1, d[k][0]):
        C += A[i]
        A1 += A[i]
        B1 += "*"
    for j in range(d[k-1][1]+1, d[k][1]):
        C += B[j]
        B1 += B[j]
        A1 += "*"
    C += A[d[k][0]]
    A1 += A[d[k][0]]
    B1 += A[d[k][0]]
for i in range(d[-1][0]+1, m):
    C += A[i]
    A1 += A[i]
    B1 += "*"
for j in range(d[-1][1]+1, n):
    C += B[j]
    B1 += B[j]
    A1 += "*"


print("Первая последовательность:\n", A1)
print("Вторая последовательность:\n", B1)
print("Итоговая последовательность:\n", C)





