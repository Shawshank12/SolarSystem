# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 17:40:33 2022

@author: Shashank
"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import barnes_hut

t_0 = 0
t = t_0
dt = 86400
t_end = 86400 * 365 * 0.5
t_array = np.arange(t_0, t_end, dt)
BIG_G = 6.67e-11

x_pos = [[],[],[],[]]
y_pos = [[],[],[],[]]
z_pos = [[],[],[],[]]

sun = barnes_hut.cel_obj(0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.989e30)
mercury = barnes_hut.cel_obj(57.909e9, 0.0, 0.0, 0.0, 47.36e3, 0.0, 0.33011e24)
venus = barnes_hut.cel_obj(108.209e9, 0.0, 0.0, 0.0, 35.02e3, 0.0, 4.8675e24)
earth = barnes_hut.cel_obj(149.596e9, 0.0, 0.0, 0.0, 29.78e3, 0.0, 5.9724e24)
mars = barnes_hut.cel_obj(227.923e9, 0.0, 0.0, 0.0, 24.07e3, 0.0, 0.64171e24)
jupiter = barnes_hut.cel_obj(778.570e9, 0.0, 0.0, 0.0, 13e3, 0.0, 1898.19e24)
saturn = barnes_hut.cel_obj(1433.529e9, 0.0, 0.0, 0.0, 9.68e3, 0.0, 568.34e24)
uranus = barnes_hut.cel_obj(2872.463e9, 0.0, 0.0, 0.0, 6.80e3, 0.0, 86.813e24)
neptune = barnes_hut.cel_obj(4495.060e9, 0.0, 0.0, 0.0, 5.43e3, 0.0, 102.413e24)

orbital_entities = [sun, mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]
positions = np.array([x.pos for x in orbital_entities])
velocities = np.array([x.vel for x in orbital_entities])
masses = np.array([x.m for x in orbital_entities])

while t<t_end:
    a_g = barnes_hut.GravAccel(positions, masses)
    for m1_id in range(len(orbital_entities)):                 
        orbital_entities[m1_id].vel += a_g[m1_id] * dt
        velocities[m1_id] = orbital_entities[m1_id].vel
    for e_id in range(len(orbital_entities)):
        orbital_entities[e_id].pos += orbital_entities[e_id].vel * dt
        positions[e_id] = orbital_entities[e_id].pos
    for i in range(1, 5):
        x_pos[i-1].append(orbital_entities[i].pos[0])
        y_pos[i-1].append(orbital_entities[i].pos[1])
        z_pos[i-1].append(orbital_entities[i].pos[2])
    t += dt
fig = plt.figure(dpi=600)
ax = plt.axes(projection='3d')
ax.axes.set_xlim3d(left=-2e11, right=2e11) 
ax.axes.set_ylim3d(bottom=-2e11, top=2e11) 
ax.axes.set_zlim3d(bottom=-1, top=1)
for j in range(4):    
    ax.plot3D(x_pos[j], y_pos[j], z_pos[j])