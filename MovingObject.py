# done by the group of: Lina Gamal Hashem - Guillaume Rouvarel - Ismail Wahdan


import numpy as np
import numpy.linalg as la

class MovingObject:
    # we use seconds as time unit and meters as distance unit
    deltaT = 2 #deltaT of 2 seconds
    a_x = 10000
    a_y = 1000
    a_z = 1000
    v = 5.5556 #m/s
    time = np.arange(0,a_x/v,deltaT)

    def __init__(self):
        a_x = MovingObject.a_x
        a_y = MovingObject.a_y
        a_z = MovingObject.a_z
        v = MovingObject.v
        time = MovingObject.time
        self.position = np.array([v*time,
                             a_y* np.sin((4*np.pi*v/a_x) * time),
                             a_z* np.sin((np.pi*v/a_x) * time)
                             ])
        
        self.velocity = np.array([v,
                             a_y*np.cos((4*np.pi*v/a_x)*time)*(4*np.pi*v/a_x),
                             a_z* np.cos((np.pi*v/a_x)*time)*(np.pi*v/a_x)])
        
        self.acc = np.array([0,
                        -a_y*(np.sin((4*np.pi*v/a_x)*time)*(4*np.pi*v/a_x)**2),
                            -a_z*(np.sin((np.pi*v/a_x)*time)*(np.pi*v/a_x)**2)])
    

    

