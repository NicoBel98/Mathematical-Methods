#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 10:46:28 2021

@author: nicolo
"""
import numpy as np
import math

G = 6.674e-8
M = 5.974e27
m =7.348e25
R = 3.844e10
omega = 2.662e-6
eps = 1e10
r = 6.37e8
rold = 4e10

while(abs(rold-r)>eps):
  rold = r
  r=((G*M)/(r*omega**2)-(r*G*m)/(omega**2*(R-r)**2))**(0.5)
  
print(r)
