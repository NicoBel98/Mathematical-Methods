#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 19:05:49 2021

@author: nicolo
"""

from Comoving_Distance import comovingdistance
#integrate is the module of scipy that performs numerical integration

#the main 

z= input("z value: ")   #initial redshift

def luminositydistance(z):
    comovingdistance*(1+z)
    
look=[] #look-back time list
redsh=[] #redshift list
while(z>0.0):
    look.append(luminositydistance(z)) #call looktime and append result
    redsh.append(z) #store z into list redsh
    z-=0.1
for i in range(len(look)): #loop over the elements of look
    print(redsh[i], look[i])