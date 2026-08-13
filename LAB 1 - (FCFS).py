at = [3,2,4,1,5]
bt = [5,4,3,2,3]

p = ["p1", "p2", "p3", "p4", "p5", ]

data = list(zip(p, at,bt))
data.sort(key=lambda x: x[1])

a = 0
b = 0
c = 0

for p,at,bt in data:

    if a < at:
        a = at
    ct = a+bt
    tat = ct - at
    wt = tat - bt

    print(p, at, bt, ct, tat, wt)

    a = ct
    b += wt
    c += tat

print("avg WT = ", b / 5)
print("avg TAT = ", c / 5)


