"""Writes 91 simulated tinker readings to the evebus"""

import evebus
import random, time

if __name__ == "__main__":
    ts = time.time ()
    
    for n in range (30):
        ts += 10
        
        evebus.write ({ "timestamp": ts,
                        "sensor": "temperature",
                        "value": random.uniform (18.0, 24.0) })

        evebus.write ({ "timestamp": ts + 1,
                        "sensor": "co2",
                        "value": random.uniform (410, 3000) })

    ## And a final staff message
    evebus.write ({ "timestamp": ts + 100,
                    "sensor": "staff_override_shutdown",
                    "value": 1.0 })
