# Raspberry Pi + Grove Switch + Grove Relay

import time
from subprocess import call
import grovepi
# Connect the Grove Switch to digital port D3
# SIG,NC,VCC,GND

switch = 2
# Connect the Grove Relay to digital port D4
# SIG,NC,VCC,GND

relay = 3
grovepi.pinMode(switch,"INPUT")
grovepi.pinMode(relay,"OUTPUT")
while True:
    try:
	print grovepi.digitalRead(switch)
        if grovepi.digitalRead(switch) == 1:
            print "pour"    
	    grovepi.digitalWrite(relay,1)
        elif grovepi.digitalRead(switch) == -1:
            call(["avrdude", "-c", "gpio", "-p", "m328p"])	   
	    time.sleep(.5)
	else:
            grovepi.digitalWrite(relay,0)
            time.sleep(.05)
    except KeyboardInterrupt:
        grovepi.digitalWrite(relay,0)
        break
    except IOError:
        print "Error"
