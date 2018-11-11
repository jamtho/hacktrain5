"""Value reader for tinkerforge co2 unit"""

from tinkerforge.bricklet_co2 import BrickletCO2

UID = "COX"

class CO2Reader ():
    def __init__ (self, ipcon):
        self.dev = BrickletCO2 (UID, ipcon)

    def get (self):
        return self.dev.get_co2_concentration ()
