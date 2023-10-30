#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 16:03:46 2021

@author: nicolo
"""
import math

t = int(input("time observation: "))
h = int(input("Tower height: "))

g = 9.81
d = int(0.5*g*t**2)

if (d>h):
    print("distanza percorsa: ", h)
else:
    print("distanza percorsa: ", d)

t2 = (2*h*g)**0.5

print("tempo trascorso: ", t2)