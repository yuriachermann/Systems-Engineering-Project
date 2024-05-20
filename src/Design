# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 16:11:24 2024

@author: G Hoepers
"""
import numpy as np
import matplotlib.pyplot as plt

#OBS: serão adotados simplificações para o caso de um planador (glider) de "brinquedo"
#OBS: L/D)max = 20-35
#OBS: Estimativa de CD0 para glider = [0.012 - 0.015]

g = 9.81                 # [m/s2]  - aceleração gravitacional
rho = 1.225              # [kg/m3] - massa especifica do ar em jvlle


#----------------------------------------------------------------
# Estimando Peso de Decolagem
#----------------------------------------------------------------


W_PL = 100/1000 * g      #  [N] - Peso de carga paga (payload) - cerca de 4 moedas de 1 real
W_C  = 0                 #  [N] - Peso da tripulacao (crew)
W_f  = 0                 #  [N] - Peso de combustível cheio (fuel)
W_E  = 300/1000 * g      #  [N] - Peso vazio (empty)

W_TO = W_PL + W_C + W_f + W_E

# Caso você tenha a fração de W_f e W_E em função do peso de decolagem, pode-se optar por
#Wf_WTO = # fração de combustível em relação ao peso de decolagem
#WE_WTO = # fração de combustível em relação ao peso de decolagem
# W_TO = (W_PL + W_C) / (1 - Wf_WTO - WE_WTO)

#----------------------------------------------------------------
# Estimando Área de Asa
#----------------------------------------------------------------

# Wing Cube Loading (WCL)
# Para um glider, 3e3 < WCL < 5e3 [kg/m3], WCL = MASSA/(AREA^1.5)
WCL = [3, 5]                               # [kg/m3]
S_min = (W_TO/(g*WCL[1]))**(2/3)           # [m2]  - área mínima
S_max = (W_TO/(g*WCL[0]))**(2/3)           # [m2]  - área máxima

# Verificando Velocidade de Estol
CLmax = [x/10 for x in range(24, 40, 2)]   #  [-]    - Coef de Sustentação Máxima - valores aleatorios
Vs    = [x/10 for x in range(15, 80, 5) ]   #  [m/s]  - Velocidade de Estol        - definir um intervalo
W_S   = []                                 #  [N/m2] - Carga alar
S     = []                                 #  [m2]   - área da asa

for i in range(0, len(CLmax)):
    W_S.append([])
    S.append([])
    for j in range(0, len(Vs)):
        W_S[i].append(  round(0.5 * rho * (Vs[j]**2) * CLmax[i], 3)  )
        S[i].append(W_TO / W_S[i][j])

     
fig, ax = plt.subplots()
for i in range(0, len(S)):
    ax.plot(S[i], Vs, label='CLmax='+str(CLmax[i]))
    ax.legend()
ax.plot(S_min*np.ones(2), [0, Vs[-1]], label='S_min')
ax.plot(S_max*np.ones(2), [0, Vs[-1]], label='S_max')
#plt.title('S_w X V_s')
plt.xlabel("Área de asa [m2]")
plt.ylabel("Velocidade de Estol [m/s]")
plt.show()
