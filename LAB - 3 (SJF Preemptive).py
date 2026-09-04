processes = [
    ["P1", 0, 4],
    ["P2", 1, 2],
    ["P3", 3, 2],
    ["P4", 2, 1]
]

time = 0
done = []
remain = {p[0]:p[2] for p in processes}

E = 0
G = 0
print ("PID AT  BT  CT  TAT WT")
while len(done) < len(processes):

    ready = []

    for p in processes:
        if p[1] <= time and p not in done:
            ready.append(p)

    if len(ready) == 0:
        time += 1
        continue

    ready.sort(key=lambda p:remain[p[0]])
    p = ready[0]

    remain[p[0]] -= 1
    time += 1

    if remain[p[0]] == 0:

        pid = p[0]
        at = p[1]
        bt = p[2]

        ct = time
        tat = ct - at
        wt = tat - bt

        print(pid, at, bt, ct, tat, wt , sep="\t")

        E += wt
        G += tat
        done.append(p)

sjf_avgwt = E / 4
sjf_avgtat = G / 4

print("Avg WT =", sjf_avgwt)
print("Avg TAT =", sjf_avgtat)