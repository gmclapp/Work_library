import math
import json
import matplotlib.pyplot as plt

class leverModel:
    ''' The lever coordinate system is defined such that the positive z axis
    is the axis of the pivot pin. The positive direction is such that a rotation
    from Park to Drive is a positive angular displacement. The x axis is parallel
    to the lever where the positive direction points toward the knob from the pivot
    the y axis completes the right-handed coordinate system.'''
    def __init__(self):
        # Define force application locations
        self.cable_pin_r = [56.25,-41.66] # mm
        self.pawl_pin_r = [69.32,0] # mm
        self.knob_r = [238,0] # mm
        self.detent_r = [71.15,26.39] # mm
        self.lockplate_r = [12.7,73.92]

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
        x = self.cable_pin_r[0]
        y = self.cable_pin_r[1]
        mag = (x**2 + y ** 2)**0.5
        theta = 1.5*math.pi
        self.cable_pin_F = [(x*math.cos(theta)-y*math.sin(theta))*self.POOP_maxF/mag,
                            (x*math.sin(theta)+y*math.cos(theta))*self.POOP_maxF/mag]
        print(self.cable_pin_F)

        LAPx = self.knob_r[0]
        LAPy = self.knob_r[1]
        LAPmag = (LAPx**2 + LAPy ** 2)**0.5
        theta = 0.5*math.pi

if __name__ == "__main__":
    Lever = leverModel()
    Lever.solve_poop_static()
        
        
