# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 19:13:53 2020

@author: Ismail
"""
import numpy as np
import matplotlib.pyplot as plt
from MovingObject import MovingObject
from Sensor import Sensor 

moving_object = MovingObject()
"""

# ========== EXERCISE 1 ==========
# Plotting trajectory,velocity and acceleration of object
position = moving_object.position
vel = moving_object.velocity
acc = moving_object.acc

fig = plt.figure()
ax = plt.axes(projection="3d")

ax.plot3D(position[0], position[1], position[2], 'gray')

ax.scatter3D(position[0],position[1], position[2], color='red',label="Ground truth position");

plt.title("3D Plane", fontsize=19)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
#plt.tick_params(axis='both', which='major', labelsize=9)
plt.legend(loc='lower right')

fig2 = plt.figure()
ax2 = plt.axes(projection='3d')
ax2.plot(vel[1], vel[2], zs=20, zdir='z',color = 'red' , label='velocity in (x, y)')
plt.title("Velocity")
ax2.set_xlabel('y')
ax2.set_ylabel('z')
ax2.set_zlabel('x')
# Data for a three-dimensional line



fig3 = plt.figure()
ax3 = plt.axes(projection='3d')
ax3.plot(acc[1], acc[2], zs=0, zdir='z', label='acceleration in (x, y)')
plt.title("Acceleration")
ax3.set_xlabel('y')
ax3.set_ylabel('z')
ax3.set_zlabel('x')



plt.show()

"""
# ========== EXERCISE 2 ==========

sensor1 = Sensor((0,100000,10000))
sensor2 = Sensor((100000,0,10000))

z_1 = sensor1.observe_object(moving_object)
z_2 = sensor2.observe_object(moving_object)
print(z_1)
# now compare measurements with ground truth
x,y,_ = moving_object.position
plt.plot(x,y,c='r',label='ground truth')


radius , angle = z_1
z_1_cartesian = np.array([[0],[100000]]) + np.array([radius * np.cos(angle), radius * np.sin(angle)])
plt.plot(z_1_cartesian[0],z_1_cartesian[1], c = 'b', label = "measurement 1")
plt.xlabel('x')
plt.ylabel('y')

plt.show()


