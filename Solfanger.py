# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 07:03:46 2022

@author: aleksam
"""

import numpy as np


pi = np.pi

slange_dia = 16 #mm
indre_dia = 200 #mm
ytre_dia = 500 #mm

N = int((ytre_dia - indre_dia) / slange_dia)

varmekapasitet_vann = 4180
Q = 0.003
delta_t = 4

# Funksjon som kalkulerer delta_t må da også være avhengig av slange_dia...

E = varmekapasitet_vann * Q * delta_t

def omkrets(diameter):
    return 2 * pi * diameter/2

def areal_sirkel(diameter):
    return pi * (diameter / 2)**2

ringer = [indre_dia]
for i in range(N):
    ring = ringer[-1]+slange_dia
    ringer.append(ring)
omkretser = [] 
for ring in ringer:
    omkretser.append(omkrets(ring))
    
areal = (areal_sirkel(ytre_dia) - areal_sirkel(indre_dia)) / 1e6

print("Antall turns:    ", N)
print("Største diameter:", ringer[-1], "mm")
print("Rørlengde:       ", round(sum(omkretser)/1e3, 2), "m")
print("Areal:           ", round(areal,2), "m^2")
print("Energi:          ", round(E,2), "W")
print("\n\n")

# Potensial
energi_areal = 1 / areal
total_energi = energi_areal * E


print("Energi på 1m^2:   ", round(total_energi, 2))




