# x^2 + 2x + 1 = 0

def g1(x):
    g = (-1)/(x+2)
    return g


def g2(x):
    g = (-1)/(x+2)
    return g


def g3(x):
    g = (-1)/(x+2)
    return g


y = []

# g1 com x0 = 0

g = []
x = []
x0 = 0
x.append(x0)
i = 0
error = 10

while error > 10**-7 and i < 10000000:

    g.append(g1(x[i]))
    x.append(g[i])
    error = abs(x[i+1] - x[i])
    i += 1

y.append(x[i-1])

# g1 com x0 = 0

g = []
x = []
x0 = 0
x.append(x0)
i = 0
error = 10

while error > 10**-7 and i < 10000000:

    g.append(g2(x[i]))
    x.append(g[i])
    error = abs(x[i+1] - x[i])
    i += 1

y.append(x[i-1])

# g1 com x0 = 0

g = []
x = []
x0 = 0
x.append(x0)
i = 0
error = 10

while error > 10**-7 and i < 10000000:

    g.append(g3(x[i]))
    x.append(g[i])
    error = abs(x[i+1] - x[i])
    i += 1

y.append(x[i-1])

print(f'Soluções {y}')
