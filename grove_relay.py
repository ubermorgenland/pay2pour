import time
import grovepi
from grovepi import *
from grove_rgb_lcd import *

# Connect the Grove Button to digital port D3
# SIG,NC,VCC,GND
button = 3
led = 4
grovepi.pinMode(button,"INPUT")

while True:
    try:
        print grovepi.digitalRead(button)
	if grovepi.digitalRead(button) == 1 :

		setText("Pouring")
		digitalWrite(led,1)     # Send HIGH to switch on LED
	        time.sleep(1)
   	        digitalWrite(led,0)     # Send LOW to switch off LED
	        setText("Pouring")
	
	setRGB(55,55,55)
	setText("Idle")

        time.sleep(.5)

    except IOError:
        print "Error"
