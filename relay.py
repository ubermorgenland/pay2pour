# Raspberry Pi + Grove Switch + Grove Relay

import time
from subprocess import call
import grovepi
from grove_rgb_lcd import * 
# Connect the Grove Switch to digital port D3
# SIG,NC,VCC,GND

switch = 8
# Connect the Grove Relay to digital port D4
# SIG,NC,VCC,GND

relay = 7
grovepi.pinMode(switch,"INPUT")
grovepi.pinMode(relay,"OUTPUT")
setText("Hello World")
token = 0
while True:
    try:
	print grovepi.digitalRead(switch)
        if grovepi.digitalRead(switch) == 1:
            token += 1
	    print "pour"
	    setText(str(token))    
	    grovepi.digitalWrite(relay,1)
        elif grovepi.digitalRead(switch) == -1:
            call(["avrdude", "-c", "gpio", "-p", "m328p"])	   
	    time.sleep(.5)
	else:
            grovepi.digitalWrite(relay,0)
            time.sleep(.05)
	setText(str(token))
    except KeyboardInterrupt:
        grovepi.digitalWrite(relay,0)
        break
    except IOError:
        print "Error"
