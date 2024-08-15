# import math
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
carpeta = ['0ml/','200ml/','300ml/','400ml/']
ruta = 'C:/Users/pedritus/Documents/UBA/Laboratorios/Laboratorio 5/P2/mediciones/decai/'
cant_archivos=[541,492,490,256] #{num%04d}
# datos = np.loadtxt('C:/Users/santiago/Desktop/Carpetas/UBA/Fisica/Laboratorios/Laboratorio 5/P2/mediciones/glicerina300ml.txt',skiprows = 4)
datos = np.loadtxt(ruta+carpeta[0]+'PIVlab_0500.txt',skiprows = 4)

# datos = np.loadtxt('C:\Users\santiago\Desktop\Carpetas\UBA\Fisica\Laboratorios\Laboratorio 5\P2\mediciones',skiprows = 4)
x = datos[:,0] #x
y = datos[:,1] #y
vx = datos[:,2] #vx
vy = datos[:,3] #vy

borders=[0.125,0.275,0.05,0.2]
x,y,vx,vy = funciones.select_field(x,y,vx,vy,borders)

sub_border = [0.18,0.22,0.117,0.147]
xsub,ysub,vxsub,vysub = funciones.select_field(x,y,vx,vy,sub_border)
vxsub= list(vxsub); vysub = list(vysub)
x_cen_max = xsub[vxsub.index(np.max(vxsub))]; 
y_cen_max = ysub[vysub.index(np.max(vysub))]

x_cen_min = xsub[vxsub.index(np.min(vxsub))]; 
y_cen_min = ysub[vysub.index(np.min(vysub))]

m_ =[] ; b_ = [] ; recta = []
for i in range(len(xsub)):
    m, b = funciones.f_(xsub[i],ysub[i],vxsub[i],vysub[i])
    m_.append(m) ; b_.append(b);


print(len(m_),len(b_)) 
#%%
#ys=[]
#ys_2=[]
n=100
i_,j_=np.random.randint(len(m_)-1, size=(2,1,len(m_)-1))
# j_=np.random.randint(5000, size=(2000))



xi=[] # me guarda los voleres en x donde se intersectan las rectas
yi=[] # me guarda los voleres en y donde se intersectan las rectas

xs=np.array([0.15,0.17,0.2,0.23,0.25,0.28,0.3])

#calculo interseccion

for i,j in zip(i_[0],j_[0]):
    #recta_(xs,m_[i],b_[i])
    #recta_(xs,m_[j],b_[j])     
    Xi = (b_[i]-b_[j]) / (m_[j]-m_[i])
    if Xi < 999999:  # este if es para que me saque los nan 
        # print(type(xi),type(m_[i]))
        Yi = m_[i] * Xi + b_[i]
        if not (Xi < 0 or Yi < 0):
            xi.append(Xi) ; yi.append(Yi);

x_c=np.mean(xi)
y_c=np.mean(yi)


# print(xi,yi)
print(np.mean(xi))
print(np.mean(yi))
#%%
                         #GRAFICO CAMPOS DE VELOCIDADES

plt.figure(figsize=(7,7))
plt.scatter(x_cen_max,y_cen_max, color ='red')
plt.scatter(x_cen_min,y_cen_min, color ='green')
plt.scatter(x_c,y_c, color ='blue')


plt.quiver(x,y,vx,vy,scale=0.5,label='Vector velocidad',color='b')
plt.xlabel('x [cm]')
plt.ylabel('y [cm]')
plt.title('Campo de velocidades')
plt.grid('True')
plt.legend()
plt.show()
# plt.savefig("Campo_velocidades_sin_glic.png")



#%%


carpeta = ['0ml/','200ml/','300ml/','400ml/']
ruta = 'C:/Users/pedritus/Documents/UBA/Laboratorios/Laboratorio 5/P2/mediciones/decai/'
cant_archivos=[541,492,490,256] #{num%04d}
# datos = np.loadtxt('C:/Users/santiago/Desktop/Carpetas/UBA/Fisica/Laboratorios/Laboratorio 5/P2/mediciones/glicerina300ml.txt',skiprows = 4)
for num in range(1,10):    
    datos = np.loadtxt(ruta+carpeta[0]+'PIVlab_'+'%04d'%num+'.txt',skiprows = 4)
    
    x = datos[:,0] #x
    y = datos[:,1] #y
    vx = datos[:,2] #vx
    vy = datos[:,3] #vy
    
    borders=[0.125,0.275,0.05,0.2]
    x,y,vx,vy = funciones.select_field(x,y,vx,vy,borders)
    
    sub_border = [0.18,0.22,0.117,0.147]
    xsub,ysub,vxsub,vysub = funciones.select_field(x,y,vx,vy,sub_border)
    vxsub= list(vxsub); vysub = list(vysub)
    
    # x_cen_max = xsub[vxsub.index(np.max(vxsub))]; 
    # y_cen_max = ysub[vysub.index(np.max(vysub))]
    
    # x_cen_min = xsub[vxsub.index(np.min(vxsub))]; 
    # y_cen_min = ysub[vysub.index(np.min(vysub))]
    
    m_ =[] ; b_ = [] ; recta = []
    for i in range(len(xsub)):
        m, b = funciones.f_(xsub[i],ysub[i],vxsub[i],vysub[i])
        m_.append(m) ; b_.append(b);
    
    i_,j_=np.random.randint(len(m_)-1, size=(2,1,len(m_)-1))
    # j_=np.random.randint(5000, size=(2000))

    xi=[] # me guarda los voleres en x donde se intersectan las rectas
    yi=[] # me guarda los voleres en y donde se intersectan las rectas

    xs=np.array([0.15,0.17,0.2,0.23,0.25,0.28,0.3])

    #calculo interseccion
    for i,j in zip(i_[0],j_[0]):
        #recta_(xs,m_[i],b_[i])
        #recta_(xs,m_[j],b_[j])     
        Xi = (b_[i]-b_[j]) / (m_[j]-m_[i])
        if Xi < 999999:  # este if es para que me saque los nan 
            # print(type(xi),type(m_[i]))
            Yi = m_[i] * Xi + b_[i]
            if not (Xi < 0 or Yi < 0):
                xi.append(Xi) ; yi.append(Yi);

    x_c=np.mean(xi)
    y_c=np.mean(yi)
    
    r, vel_theta = funciones.polares(x-x_c,y-y_c,vx,vy) 

    rnueva , vnueva = funciones.delete_nan(r, vel_theta)  
          
    #ordeno la lista con data frame usando sort

    r_arr , v_arr = funciones.ordenar(rnueva, vnueva)

    plt.figure()
    plt.grid(True)
    plt.scatter(r_arr,abs(v_arr))
    plt.show()
    
    
    
    
