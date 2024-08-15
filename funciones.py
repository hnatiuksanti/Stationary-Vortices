import math
import numpy as np
import pandas as pd

def alfa(vx,vy):
    a = np.tan(vy/vx)
    return a

def thita(a):
    thita = a - np.pi/2
    return thita 

def f_(x_0,y_0,vx,vy):
    m = np.tan(thita(alfa(vx,vy)))
    m = -vx/vy
    b = y_0 - m*x_0
    return [m,b]

def recta_(x,m,b):
    y = m*x + b
    return y   

# Cambio de variables de cartesianas a Polares.
def polares(x_centro,y_centro,vx,vy):
    #transformo a polares 
    r= np.sqrt((x_centro)**2 + (y_centro)**2)
    theta = np.arctan(y_centro/x_centro)
        
    #hago las derivadas
    dx=((-y_centro/((x_centro**2)+(y_centro**2)))*vx)
    dy=((x_centro/((x_centro**2)+(y_centro**2)))*vy)
    
    #calculo las velocidades haciendo regla de la cadena
    #vel_r=sp.diff(r,x_centro) + sp.diff(r,y_centro)
    vel_theta = r*(dx+dy)
    return [r, vel_theta] 

#Genero dos listas nuevas sacando los puntos que son nan
def delete_nan(r, vel_theta):
    rnueva=[] ; vnueva = []
    for i,j in zip(r,vel_theta):
        if j < 999999: 
            vnueva.append(j)
            rnueva.append(i)
    return [rnueva,vnueva]

#Me quedo solo con las velocidad entre los bordes. (quita las velocidades 'feas' de los bordes)
def quitar_bordes(x,y,vx,vy,bordes):
    x_n=[] ; y_n=[] ; 
    vx_n=[]
    vy_n=[] 
    for i in range(len(x)):
        if x[i] > bordes[0] and y[i] > bordes[1] :
            y_n.append(y[i]) ; x_n.append(x[i])
            vy_n.append(vy[i]) ; vx_n.append(vx[i])
    return [np.asarray(x_n),np.asarray(y_n),np.asarray(vx_n),np.asarray(vy_n)]

def ordenar(rnueva,vnueva):
    df = pd.DataFrame()
    df['r']=rnueva
    df['v']=vnueva
    df = df.sort_values('r')
    return [ np.array(df['r']) , np.array(df['v'])]

#Calculo chi^2 para el ajuste. 
def chisq(datos,ajuste,sigma):
    chi = 0
    for x in datos:
        chi = chi + ((x - ajuste[datos.index(x)])/sigma)**2
    return chi

#Calcula sigma y chi.
def sigma(intervalo,X):
    s = 0 ; chi = 0
    for x in intervalo:
        s = (x - X)**2 + s
    sig = np.sqrt(s)/(np.sqrt(len(intervalo)))
    for x in intervalo:
        chi = chi + ((x - X)/sig)**2
    return [sig, chi] 

#%%

'''                                 -----------DECAIMIENTO-----------                           '''
def dec_del_nan(r, vel_theta):
    rnueva=[] ; vnueva = []
    for i,j in zip(r,vel_theta):
        if j < 999999: 
            vnueva.append(j)
            rnueva.append(i)
    return [rnueva,vnueva]


def select_field(x,y,vx,vy,borders):
    x_i,x_s,y_i,y_s=borders
    x_n=[] ; y_n=[] ; 
    vx_n=[] ; vy_n=[] 
    for i in range(len(x)):
        if x[i] > x_i and  y[i] > y_i and x[i] < x_s and y[i] < y_s :
            y_n.append(y[i]) ; x_n.append(x[i])
            vy_n.append(vy[i]) ; vx_n.append(vx[i])
    return [np.asarray(x_n),np.asarray(y_n),np.asarray(vx_n),np.asarray(vy_n)]


