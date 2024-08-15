import math
import numpy as np
import os
from matplotlib import pyplot as plt
import scipy.optimize
import sympy as sp 
import pandas as pd
from IPython import get_ipython

import funciones
# get_ipython().run_line_magic('matplotlib', 'inline')
get_ipython().run_line_magic('matplotlib', 'qt5')

#%%
'''CARGO DATOS'''

# datos = np.loadtxt('C:/Users/santiago/Desktop/Carpetas/UBA/Fisica/Laboratorios/Laboratorio 5/P2/mediciones/glicerina300ml.txt',skiprows = 4)
datos = np.loadtxt('C:/Users/pedritus/Documents/UBA/Laboratorios/Laboratorio 5/P2/mediciones/promvideo2.txt',skiprows = 4)
# datos = np.loadtxt('C:\Users\santiago\Desktop\Carpetas\UBA\Fisica\Laboratorios\Laboratorio 5\P2\mediciones',skiprows = 4)
x = datos[:,0] #x
y = datos[:,1] #y
vx = datos[:,2] #vx
vy = datos[:,3] #vy

m_ =[] ; b_ = [] ; recta = []
for i in range(len(x)):
    m, b = funciones.f_(x[i],y[i],vx[i],vy[i])
    m_.append(m) ; b_.append(b);

                         #GRAFICO CAMPOS DE VELOCIDADES
bordes = [[0,0],[0.1284,0.0389],[0,0],[0.06012,0.01147],[0.0677,0.0143]] #Cada borde corresponde a gli0ml, gli 100ml y asi 
x,y,vx,vy = funciones.quitar_bordes(x,y,vx,vy,bordes[0]) # Me quedo solo con las velocidades dentro de los bordes 
plt.figure(figsize=(7,7))
plt.quiver(x,y,vx,vy,scale=0.5,label='Vector velocidad',color='b')
plt.xlabel('x [cm]')
plt.ylabel('y [cm]')
plt.title('Campo de velocidades')
plt.grid('True')
plt.legend()
plt.show()
plt.savefig("Campo_velocidades_sin_glic.png")

#%%
''' CAMBIO DE VARIABLES '''

#Defino los centros para medicion (esto se hizo a ojo)
centros = [[0.202,0.122],[0.22511,0.130],[0.2098,0.1173],[0.1510,0.1104] , [0.1664, 0.1068]]

x_centro= x-centros[4][0]
y_centro=y-centros[4][1]

r, vel_theta = funciones.polares(x_centro, y_centro,vx,vy) 

rnueva , vnueva = funciones.delete_nan(r, vel_theta)  
      

#ordeno la lista con data frame usando sort
r_arr , v_arr = funciones.ordenar(rnueva, vnueva)
plt.figure()
plt.grid(True)
plt.scatter(r_arr,abs(v_arr))
plt.show()

#%%
'''PROMEDIO DE LAS VELOCIDADES TANGENCIALES Y EL RADIO PARA SUAVIZAR LA DISPERCION'''
# (El codigo no esta optimizado, puede que tarde un ratito en realizar los promedios!!!)

r_list = list(r_arr); v_list = list(abs(v_arr))
r_izq= [] ; r_der = [] ; r_interval = [] ; r_prom = []  
v_izq = [] ; v_der = [] ; v_interval = [] ; v_prom = []
sigma_r = [] ; sigma_v = []

for r,v in zip(r_list,v_list): 
    if r < r_list[v_list.index(np.max(abs(v_arr)))]:
        v_izq.append(v)
        r_izq.append(r)
        v_interval.append(v)
        r_interval.append(r)
        if len(r_interval) == 10 : 
            v_prom.append(np.mean(v_interval))
            r_prom.append(np.mean(r_interval))
            sigma_r.append(funciones.sigma(r_interval,r_prom[-1])[0]/np.sqrt(len(r_interval)))
            sigma_v.append(funciones.sigma(v_interval,v_prom[-1])[0]/np.sqrt(len(v_interval)))
            r_interval = []; v_interval = []
            
    if r >= r_list[v_list.index(np.max(abs(v_arr)))]:
        v_der.append(v)
        r_der.append(r)
        v_interval.append(v)
        r_interval.append(r)
        if len(r_interval) == 200 : 
            v_prom.append(np.mean(v_interval))
            r_prom.append(np.mean(r_interval))
            sigma_r.append(funciones.sigma(r_interval,r_prom[-1])[0]/np.sqrt(len(r_interval)))
            sigma_v.append(funciones.sigma(v_interval,v_prom[-1])[0]/np.sqrt(len(v_interval)))
            r_interval = []; v_interval = []

# np.savetxt('promedios_400.txt', [r_prom,v_prom,sigma_r,sigma_v], delimiter= ',')
plt.figure()        
# plt.scatter(r_izq,v_izq, label = 'Izq')
# plt.scatter(r_der,v_der, label = 'Der')
plt.scatter(r_list,v_list, label = 'Datos')
plt.errorbar(r_prom,v_prom, fmt = 'o',color ='red', xerr = sigma_r ,yerr = sigma_v, label = 'Promedios')
plt.legend()
plt.show()


#%%
''' ver txt promedios '''
datos = np.loadtxt('C:/Users/pedritus/Documents/UBA/Laboratorios/Laboratorio 5/P2/mediciones/promedios_400.txt', delimiter= ',')

plt.errorbar(datos[0], datos[1], xerr= datos[2] , yerr=datos[3])


