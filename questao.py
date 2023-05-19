# Tolueno
Tc = 591.8
Pc = 41.06*10**5
R = 8.314
a = 0.42748*(R**2)*(Tc**2)/Pc
b = 0.08664*R*Tc/Pc
beta = (b*Pc)/(R*Tc)
q = a/(b*R*Tc)

# Liquido

print(f'Tolueno:')

z0_tl = 1.05*beta
z_tl = []
z_tl.append(z0_tl)
erro_tl = 10
k = 0

for k in range(100000):
    z_tl.append(beta + z_tl[k]*(z_tl[k]+beta)
                * ((1+beta-z_tl[k])/(q*beta)))
    erro_tl = abs(z_tl[k]-z_tl[k-1])/max(z_tl[k], z_tl[k-1])

print(z_tl[k])
print(erro_tl)

# Vapor

z0_tv = 1
z_tv = []
z_tv.append(z0_tv)
erro_tv = 10
k = 0

for k in range(100000):
    z_tv.append(1 + beta - q*beta *
                ((z_tv[k]-beta)/(z_tv[k]*(z_tv[k] + beta))))
    erro_tv = abs(z_tv[k]-z_tv[k-1])/max(z_tv[k], z_tv[k-1])

print(z_tv[k])
print(erro_tv)

# Água
print(f'\nÁgua:')
Tc = 647.1
Pc = 220.55*10**5
R = 8.314
a = 0.42748*(R**2)*(Tc**2)/Pc
b = 0.08664*R*Tc/Pc
beta = (b*Pc)/(R*Tc)
q = a/(b*R*Tc)

# Liquido

z0_tl = 1.05*beta
z_tl = []
z_tl.append(z0_tl)
erro_tl = 10
k = 0

for k in range(100000):
    z_tl.append(beta + z_tl[k]*(z_tl[k]+beta)
                * ((1+beta-z_tl[k])/(q*beta)))
    erro_tl = abs(z_tl[k]-z_tl[k-1])/max(z_tl[k], z_tl[k-1])

print(z_tl[k])
print(erro_tl)

# Vapor

z0_tv = 1
z_tv = []
z_tv.append(z0_tv)
erro_tv = 10
k = 0

for k in range(100000):
    z_tv.append(1 + beta - q*beta *
                ((z_tv[k]-beta)/(z_tv[k]*(z_tv[k] + beta))))
    erro_tv = abs(z_tv[k]-z_tv[k-1])/max(z_tv[k], z_tv[k-1])

print(z_tv[k])
print(erro_tv)
