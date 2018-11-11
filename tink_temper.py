"""Value reader for tinkerforge tempareature unit"""

from tinkerforge.bricklet_temperature import BrickletTemperature

UID = "OXJ"

class TempReader ():
    def __init__ (self, ipcon):
        self.dev = BrickletTemperature (UID, ipcon)

    def get (self):
        return self.dev.get_temperature () / 100.0
