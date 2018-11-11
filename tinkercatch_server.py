"""Gathers data from the tinkerforge sensors and writes to the event bus"""

from tinkerforge.ip_connection import IPConnection
import tink_temper, tink_co2
import evebus
import time

HOST = "localhost"
PORT = 4223

DELAY_SECS = 5

if __name__ == '__main__':
    ipcon = IPConnection ()

    temper = tink_temper.TempReader (ipcon)
    co2    = tink_co2.CO2Reader (ipcon)

    ipcon.connect (HOST, PORT)

    while True:
        ts = time.time ()
        
        t = temper.get ()
        evebus.write ({ "timestamp": ts,
                        "sensor": "temperature",
                        "value": t })

        c = c2.get ()
        evebus.write ({ "timestamp": ts,
                        "sensor": "co2",
                        "value": c })

        time.sleep (DELAY_SECS)
    
