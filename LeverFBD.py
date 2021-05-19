import json
import numpy as np
import matplotlib.pyplot as plt

def RotateZ(vector,deg):
    '''vector = numpy array [x,y,z], degrees = rotation
    Returns a unit vector rotated counter clockwise about z by degrees.'''
    r = deg * np.pi/180
    mag = np.linalg.norm(vector)
    R = np.array([[np.cos(r),-1*np.sin(r),0],
                    [np.sin(r),np.cos(r),0],
                    [0,0,1]])
    vector_new = np.matmul(R,vector)/mag
    return(vector_new)

class leverModel:
    ''' The lever coordinate system is defined such that the positive z axis
    is the axis of the pivot pin. The positive direction is such that a rotation
    from Park to Drive is a positive angular displacement. The x axis is parallel
    to the lever where the positive direction points toward the knob from the pivot
    the y axis completes the right-handed coordinate system.'''
    def __init__(self):
        # Define force application locations
        self.cable_pin_r = np.array([56.25,-41.66,0]) # mm
        self.pawl_pin_r = np.array([69.32,0,0]) # mm
        self.knob_r = np.array([238,0,0]) # mm
        self.detent_r = np.array([71.15,26.39,0]) # mm
        self.lockplate_r = np.array([12.7,73.92,0])

        # Define force vectors
        self.cable_pin_F = 0 # N
        self.pawl_pin_F = 0
        self.knob_F = 0
        self.detent_F = 0

        # Load paradigms
        # Max pull out of park
        self.POOP_maxF = 450 # N, scalar
        # Park forcible override
        # Neutral forcible override
        # Park overtravel
        # Drive overtravel
        # Normal operation

    def solve_poop_static(self):
        self.cable_pin_F = RotateZ(self.cable_pin_r,270)
        self.cable_pin_F *= self.POOP_maxF
        print(self.cable_pin_F)
        self.poop_T = np.cross(self.cable_pin_r,self.cable_pin_F)
        print(self.poop_T)

        self.knob_F = -1 * np.cross(self.poop_T,self.knob_r)/np.dot(self.knob_r,self.knob_r)
        print(self.knob_F)


if __name__ == "__main__":
    Lever = leverModel()
    Lever.solve_poop_static()
        
        
