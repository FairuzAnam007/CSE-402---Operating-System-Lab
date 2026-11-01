processes = [
    ["P1", 0, 3, 4],
    ["P2", 3, 2, 0],
    ["P3", 1, 2, 2],
    ["P4", 2, 1, 1]
]

time = 0
t_wt = 0
t_tat = 0
done = []

print("P  AT   BT  PR  CT  TAT WT")

while len(done) < len(processes):

    ready = []

    for p in processes:
        if p[1] <= time and p not in done:
            ready.append(p)

    if len(ready) == 0:
        time += 1
        continue

    ready.sort(key=lambda x: x[3])
    p = ready[0]

    pid = p[0]
    at = p[1]
    bt = p[2]
    priority = p[3]

    ct = time + bt
    tat = ct - at
    wt = tat - bt

    print(pid, at, bt, priority, ct, tat, wt , sep = "\t")

    time = ct
    t_wt += wt
    t_tat += tat

    done.append(p)

print("Average WT =", t_wt / len(processes))
print("Average TAT =", t_tat / len(processes))

