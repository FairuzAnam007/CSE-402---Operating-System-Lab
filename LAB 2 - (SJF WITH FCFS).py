print ('------FCFS------')
at = [2,3,0,1,1]
bt = [5,1,2,3,6]

p = ["P1", "P2", "P3", "P4", "P5"]

data = list(zip(p, at, bt))
data.sort(key=lambda x: x[1])

a = 0
b = 0
c = 0

for pid, at1, bt1 in data:

    if a < at1:
        a = at1

    ct = a + bt1
    tat = ct - at1
    wt = tat - bt1

    print(pid, at1, bt1, ct, tat, wt)

    a = ct
    b += wt
    c += tat

f_avgwt = b / 5
f_avgtat = c / 5

print("Avg WT =", f_avgwt)
print("Avg TAT =", f_avgtat)


print ('------SJF------')

processes = [
    ["P1", 2, 5],
    ["P2", 3, 1],
    ["P3", 0, 2],
    ["P4", 1, 3],
    ["P5", 1, 6]
]

D = 0
E = 0
G = 0
F = []

while len(F) < len(processes):

    ready = []

    for p in processes:
        if p[1] <= D and p not in F:
            ready.append(p)

    if len(ready) == 0:
        D += 1
        continue

    ready.sort(key=lambda p: p[2])
    p = ready[0]

    pid = p[0]
    at = p[1]
    bt = p[2]

    ct = D + bt
    tat = ct - at
    wt = tat - bt

    print(pid, at, bt, ct, tat, wt)

    D = ct
    E += wt
    G += tat

    F.append(p)

sjf_avgwt = E / 5
sjf_avgtat = G / 5

print("Avg WT =", sjf_avgwt)
print("Avg TAT =", sjf_avgtat)

print("\n----- Comparison -----")

print("FCFS Avg WT =", f_avgwt)
print("FCFS Avg TAT =", f_avgtat)

print("SJF Avg WT =", sjf_avgwt)
print("SJF Avg TAT =", sjf_avgtat)

if sjf_avgwt < f_avgwt:
    print("SJF is better.")
elif f_avgwt < sjf_avgwt:
    print("FCFS is better.")
else:
    print("Both are same.")
