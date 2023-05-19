import math

import matplotlib.pyplot as plt

# Programa feito por RCCO em 04/04/2023 para disciplina de Termodinâmica Aplicada no Programa de Engenharia Química da COPPE/UFRJ

Sref_a = 0  # J/K para Tref = 25ºC e densidade = 50mol/m^3
Tref_a = 25+273.15  # K
T_a0 = 92+273.15  # K
n_a = 50  # mol
v_a = 1  # m^3
Cv_a = 21  # J/(molK)

Sref_b = 0  # J/K para Tref = 25ºC e densidade = 100mol/m^3
Tref_b = 25+273.15  # K
T_b0 = 28+273.15  # K
n_b = 300  # mol
v_b = 3  # m^3
Cv_b = 29  # J/(molK)


# Letra A
S_a = Sref_a + n_a*Cv_a*math.log(T_a0/Tref_a)
S_b = Sref_b + n_b*Cv_b*math.log(T_b0/Tref_b)
S_total = S_a + S_b

print(
    f'Letra a: A entropia total do sistema no instante inicial é: {S_total:.2f} J/K\n')

# Letra B e C

T_f = (n_b*Cv_b*T_b0 + n_a*Cv_a*T_a0)/(n_b*Cv_b + n_a*Cv_a)

Q_a = n_a*Cv_a*(T_f-T_a0)

print(
    f'Letra b: A quantidade de calor necessária para atingir o equilíbrio é: {Q_a:.2f} J\n')

print(
    f'Letra c: A temperatura de A no equilibro é igual a temperatura de B no equilíbrio e ambas são iguais a: {T_f:.2f} K\n')

# Letra D e E

Q_vetor = range(1, 100000, 1000)
S_a_vetor = []
S_b_vetor = []
S_total_vetor = []
T_a = []
T_b = []

for i, Q in enumerate(Q_vetor):
    T_a.append(T_a0 + Q/(n_a*Cv_a))
    T_b.append(T_b0 - Q/(n_b*Cv_b))
    S_a_vetor.append(S_a + n_a*Cv_a*math.log(T_a[i]/Tref_a))
    S_b_vetor.append(S_b + n_b*Cv_b*math.log(T_b[i]/Tref_b))
    S_total_vetor.append(S_a_vetor[i]+S_b_vetor[i])
