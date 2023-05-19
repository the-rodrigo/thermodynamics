'''
A - metano
B - CO2
'''

import math

def set_Tr(T,Tc):
    return T/Tc

def get_k(w):
    return 0.48508 + 1.55171*w - 0.1761*(w**2)

def get_alfa(k,Tr):
    return (1 + k*(1 - math.sqrt(Tr)))**2

def get_ac(Tc,Pc):
    return 0.42748*(R**2)*(Tc**2)/Pc

def get_ai(T,Tc,Pc,w):
    k = get_k(w)
    Tr = set_Tr(T,Tc)
    alfa = get_alfa(k,Tr)
    ac = get_ac(Tc,Pc)
    return ac*alfa

def get_bi(Tc,Pc):
    return 0.08664*R*Tc/Pc

def SRK(T,v,a,b):
    return (R*T)/(v - b) - a/(v*(v-b))


# Dados Termodinâmicos
T = 200 #K
V = 0.2 #m**3
R = 8.314 #J/molK
n_components = 2

# Dados molares
na = 7 #mol
nb = 3 #mol
n = na + nb
x_vet = [na/n,nb/n]

# Dados Criticos

Tca = 190.6 #K
Tcb = 304.2 #K
Pca = 45.99*10**5 #Pa
Pcb = 73.83*10**5 #Pa
wa = 0.012
wb = 0.224

# Criando vetores
Tc_vet = [Tca,Tcb]
Pc_vet = [Pca,Pcb]
w_vet = [wa,wb]

# Calculo de Parametros SRK

b = 0 
a = 0
for i in range(n_components):
    b += x_vet[i]*get_bi(Tc_vet[i],Pc_vet[i])
    for j in range(n_components):
        a += x_vet[i]*x_vet[j]*math.sqrt(get_ai(T,Tc_vet[i],Pc_vet[i],w_vet[i])*get_ai(T,Tc_vet[j],Pc_vet[j],w_vet[j]))

# Calculo da P, v e z

v = V/n
P = SRK(T,v,a,b)
z = (P*v)/(R*T)

# Calculo de fugacidade
fugacity_vet = []

for i in range(n_components):
    # 1º Fração
    first_frac = get_bi(Tc_vet[i],Pc_vet[i])*(z-1)/b
    
    # 2º Fração
    second_frac = -math.log(P*(v-b)/(R*T))
    
    # 3º Fração
    sum_ai = 0

    for j in range(n_components):
        sum_ai += x_vet[j]*math.sqrt(get_ai(T,Tc_vet[i],Pc_vet[i],w_vet[i])*get_ai(T,Tc_vet[j],Pc_vet[j],w_vet[j]))

    third_frac = (a/(b*R*T))*(get_bi(Tc_vet[i],Pc_vet[i])/b - 2*sum_ai/a)*(math.log((v+b)/v))

    fugacity = math.exp(first_frac + second_frac + third_frac)
    fugacity_vet.append(fugacity)

print(fugacity_vet)