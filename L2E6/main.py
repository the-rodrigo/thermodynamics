import math

from numpy import linspace


def initial_value(P) -> int or float:
    return R*T/P


def get_value(P, v) -> int or float:
    return (initial_value(P) + b - ((a*(v-b))/(P*v*(v+b))))

# Amônia - Isotérmico


R = 8.314  # J/molK
Tc = 405.7  # K
Pc = 112.8*(10**5)  # Pa
T = 373.15  # K
Tr = T/Tc
alfa = 1/(math.sqrt(Tr))
a = (0.42748*alfa*(R**2)*(Tc**2))/Pc  # Pa*(m^3/mol)^2
b = .08664*R*Tc/Pc  # m^3/mol

pressures = linspace(10**5, 50*10**5, 100)
v_values = []

# Loop

for P in pressures:
    v = []  # Variavel
    g = []  # Função

    v.append(initial_value(P))
    i = 0
    error = 10  # Valor alto aleatório para setar erro inicial
    tolerance = 10**-100
    safety_loops = 1000

    while error > tolerance and i < safety_loops:

        g.append(get_value(P, v[i]))
        v.append(g[i])
        error = abs(v[i+1] - v[i])
        i += 1

    v_values.append(v[len(v)-1])

vf = v_values[len(v_values) - 1]
vi = v_values[0]

W = (R*T*math.log((vf - b)/(vi - b))) + \
    ((a/b)*math.log((vi*(vf+b))/(vf*(vi+b))))  # J/mol

for value in v_values:
    print(value)

print(W)
