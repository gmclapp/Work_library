import json
import matplotlib.pyplot as plt

class leverModel:
    def __init__(self):
        # Define force application locations
        self.cable_pin_r = [0,0]
        self.pawl_pin_r = [0,0]
        self.knob_r = [0,0]
        self.detent_r = [0,0]

        # Define force vectors
        self.cable_pin_F = 0
        self.pawl_pin_F = 0
        self.knob_F = 0
        self.detent_F = 0

        # Load paradigms
        # Max pull out of park
        # Park forcible override
        # Neutral forcible override
        # Park overtravel
        # Drive overtravel
        # Normal operation
        
