"""Reads events from the eventbus and controls the HVAC system"""

import evebus
import time


##  ======================================================================
##  Constants

TARGET_TEMP_C = 21.0

HVAC_SCALE = 0.13


##  ======================================================================
##  HVAC control is virutal serial

HVAC_OUTPUT = "/dev/hvacctl"
## HVAC_OUTPUT = "/dev/stdout"

def writeHvac (val):
    with open(HVAC_OUTPUT, "w") as f:
        f.write (str(val))
        f.write ("\n")


##  ======================================================================
##  HVAC effect model

def hvacModelVal (ctemp, co2grad):
    dtemp = TARGET_TEMP_C - ctemp
    rawOut = dtemp * HVAC_SCALE
    if co2grad > 0.3:
        return rawOut * co2grad * 0.1
    else:
        return rawOut
        
        
##  ======================================================================
##  main ()

curTemp = None

lastCO2_ts   = None
lastCO2_val  = None
lastCO2_grad = None

overrideEngaged = False

if __name__ == '__main__':
    lastTime = time.time ()
    
    while True:
        newEvents = evebus.after (lastTime)

        for e in newEvents:
            print "HVAC GOT EVENT: ", e
            
            if overrideEngaged:
                writeHvac (0)
                break

            if e["sensor"] == "staff_override_shutdown":
                overrideEngaged = True
                writeHvac (0)
                break
            
            elif e["sensor"] == "co2":
                if lastCO2_val is not None:
                    dt = e["timestamp"] - lastCO2_ts
                    dv = e["value"] - lastCO2_val
                    lastCO2_grad = dv/dt
                    hv = hvacModelVal (curTemp, lastCO2_grad)
                    writeHvac (hv)
                lastCO2_ts  = e["timestamp"]
                lastCO2_val = e["value"]
                
            elif e["sensor"] == "temperature":
                curTemp = e["value"]
                if lastCO2_grad is not None:
                    hv = hvacModelVal (curTemp, lastCO2_grad)
                    writeHvac (hv)

        lastTime = time.time ()
        time.sleep (1)

