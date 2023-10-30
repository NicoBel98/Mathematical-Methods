#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 10:26:02 2022

@author: nicolo
"""

import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import norm

x1 = np.array([3., 0., 3.], float)
y1 = np.array([4., 0., 0.], float)
m = np.array([3., 4., 5.], float)
vx1 = np.array([0.,0.,0.], float)
vy1 = np.array([0.,0.,0.], float)

print(x1,y1) 
print(vx1,vy1) 
print(m)

G = 1.


t0 = 0
tf = 5
h = 1e-6
t = np.arange(t0, tf+h, h)

# Accelerazione calcola ax, ay per ogni corpo, ogni riga corrisponde ad un corpo diverso

def acc(x,y,m):
    N = len(m)
    ax = np.zeros(N,float)
    ay = np.zeros(N,float)
    
    for i in range(N):
        for j in range(N):
            if i!=j:
                module = np.sqrt((x[i]-x[j])**2+(y[i]-y[j])**2)
                ax[i] += -G*m[j]*(x[i]-x[j])/(module)**3
                ay[i] += -G*m[j]*(y[i]-y[j])/(module)**3
                
    return ax, ay
# La prima colonna degli array corrisponde alla posizione iniziale dei corpi, dopo si calcola il valore al tempo t+h, e quindi colonna j+h
def euler(x1,y1,vx1,vy1,m,h,t):
    N = len(m)
    x = np.zeros([N, len(t)],float)
    x[:,0] = x1
    y = np.zeros([N, len(t)],float)
    y[:,0] = y1
    vx = np.zeros([N, len(t)],float)
    vx[:,0] = vx1
    vy = np.zeros([N, len(t)],float)
    vy[:,0] = vy1
    for j in range(0, len(t)-1):
            ax,ay = acc(x[:,j],y[:,j],m) #La funzione acc usa l'intera colonna per calcolare ax ed ay
            x[:,j+1]=x[:,j]+vx[:,j]*h
            y[:,j+1]=y[:,j]+vy[:,j]*h
            vx[:,j+1]=vx[:,j]+ax*h
            vy[:,j+1]=vy[:,j]+ay*h
            
    return x,y,vx,vy

x,y,vx,vy = euler(x1,y1,vx1,vy1,m,h,t)

print(x,y)

plt.plot(x[0,:],y[0,:])
plt.plot(x[1,:],y[1,:])
plt.plot(x[2,:],y[2,:])
plt.show()
