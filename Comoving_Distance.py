#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 18:56:24 2021

@author: nicolo
"""
import scipy.integrate as integrate
#integrate is the module of scipy that performs numerical integration

def comovingdistance(z): #definition of new function looktime. 
# This function takes one argument (z)

    H0=67.2 #Hubble constant in km/s/Mpc
    convert=1e5/3.086e24*3.1536e7*1e9 
    #converts from km/s/Mpc to Gyr

    OmegaM=0.2726   #omega matter, parameter from cosmology
    OmegaL= 0.7274  #omega lambda, parameter from cosmology

    integrand = lambda x: 1./((OmegaM*(1.+x)**3.+OmegaL)**0.5)
    #integrand is the function I want to integrate between 0 and z

    ltime=integrate.quad(integrand, 0.0, z)
    #ltime is an array of 2 elements. ltime[0]= result of integral
    #ltime[1] error

    look=ltime[0]
    look/=(H0*convert)
    return look #function looktime returns look, which 
    #is the look back time at redshift z in comoving framework



#the main 

z=10.   #initial redshift
look=[] #look-back time list
redsh=[] #redshift list
while(z>0.0):
    look.append(comovingdistance(z)) #call looktime and append result
    redsh.append(z) #store z into list redsh
    z-=0.1
for i in range(len(look)): #loop over the elements of look
    print(redsh[i], look[i]) #prints redshift and 
#corresponding look back time list
