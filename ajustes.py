import math
import numpy as np
import os
from matplotlib import pyplot as plt
import scipy.optimize
import sympy as sp 
import pandas as pd
from IPython import get_ipython
from scipy.optimize import curve_fit

import funciones
# get_ipython().run_line_magic('matplotlib', 'inline')
get_ipython().run_line_magic('matplotlib', 'qt5')
#%%

ruta = 'C:/Users/pedritus/Documents/UBA/Laboratorios/Laboratorio 5/P2/mediciones/'
archivos = ['promedios_agua','promedios_200','promedios_300','promedios_400']
names = ['glicerina : 0 ml ','glicerina : 200 ml','glicerina : 300 ml','glicerina : 400 ml']
c_list = []
for name, archivo in zip(names,archivos): 
    datos = np.loadtxt(ruta+f'{archivo}.txt', delimiter= ',')
    
    r = list(datos[0]); rerr = list(datos[2]); 
    v = list(datos[1]); verr = list(datos[3]);
    
    c_list.append(r[v.index(np.max(abs(datos[1])))])
    plt.figure(num=1,figsize=(7.5,6))
    # plt.title('Vel promedio vs r promedio', size = 14)
    plt.grid(True)
    plt.xlabel('r [m]', size = 12)
    plt.ylabel('v_theta [m/s]', size = 12)
    plt.errorbar(datos[0], datos[1], fmt = 'o',xerr= datos[2] , yerr=datos[3], label =f'{name}')    
    plt.legend()
plt.show()
# plt.savefig(ruta+'v_prom vs r_prom.png', dpi = 1000)

#%%
# usar [:40] ajuste y [1:41] para chi. para agua 

datos = np.loadtxt(ruta+'promedios_300.txt', delimiter= ',')
radios = [0.0185,0.0109,0.0159,0.0185]
r = list(datos[0]); rerr = list(datos[2]); 
v = list(datos[1]); verr = list(datos[3]);
c=radios[2]#radio en m
r_1= r[len(r)-1]
v_1=v[len(v)-1]

#donde C es la vorticidad
def func_burgers(x,C): 
    return ((C*c**2)/x)*(1-np.exp(-(x**2/c**2))) 

C0= [(v_1/r_1)/(1-np.exp(-(r_1)**2/c**2))] #parametro inicial 

popt,pcov = curve_fit(func_burgers,r[:45],v[:45],p0=C0)

perr = np.sqrt(np.diag(pcov))

x=np.linspace(0,0.1,100)


ajuste = func_burgers(x, *popt)
chisq = funciones.chisq(v[1:], ajuste[1:99], np.sqrt(pcov[0]))
    
print(popt[0], np.sqrt(np.diag(pcov)))

n=75 ; h = 0.001 # n es la cantidad de datos y sirve para calcular el chi reducido. h es un parametro de altura de plt.annotate. 

#plt.plot(rnueva,np.absolute(vnueva),'.',label='datos sin promediar')
plt.figure()
plt.grid(True)
plt.errorbar(r[:40],v[:40],fmt = '.',xerr=rerr[:40],yerr=verr[:40], label='datos promediados',color='r')  
plt.plot(x,func_burgers(x,*popt),'--', label='Ajuste',color='blue')
plt.annotate(f'chisq = {chisq}', (0.05,0.015-h))
plt.annotate(f'chisq_redu = {chisq/n}', (0.05,0.014-h))
plt.annotate(f'omega = {popt[0]}', (0.05,0.013-h))
plt.annotate(f'omega_err = {np.sqrt(pcov[0])}', (0.05,0.012-h))
plt.xlabel('Radio [m]')
plt.ylabel('Velocidad [m/s]')
plt.title(f'{archivos[2]}')
plt.legend()
plt.show()