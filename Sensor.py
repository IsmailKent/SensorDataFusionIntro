# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 18:33:46 2020

@author: Ismail
"""

import numpy as np
from MovingObject import MovingObject

class Sensor:
        
        sigma_r = 10 #meter
        sigma_phi = np.deg2rad(0.1) #rad
        
        def __init__(self, position:tuple):
            self.x_s , self.y_s , self.z_s = position
        
        
        
        def observe_object(self,moving_object: MovingObject):
            #extract position list in the 2 dimensions we observe
            x,y, _ = moving_object.position
            z = np.zeros((2,x.size))
            z[0] = np.sqrt((x-self.x_s)**2 + (y-self.y_s)**2 + self.z_s**2)
            z[1] = np.arctan2(y-self.y_s,x-self.x_s)
            noise = np.random.normal(0,1,(2,x.size)) * np.array([[Sensor.sigma_r],[Sensor.sigma_phi]])
            print(noise)
            z += noise
            return z
        
mo = MovingObject()
            