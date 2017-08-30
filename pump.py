import RPi.GPIO as GPIO   # Import the GPIO library.
import signal
import sys
import time               # Import time library

GPIO.setmode(GPIO.BOARD)  # Set Pi to use pin number when referencing GPIO pins.
                         # Can use GPIO.setmode(GPIO.BCM) instead to use
                         # Broadcom SOC channel names.

GPIO.setup(12, GPIO.OUT)  # Set GPIO pin 12 to output mode.
pwm = GPIO.PWM(12, 100)   # Initialize PWM on pwmPin 100Hz frequency


def signal_handler(signal, frame):
   pwm.stop()
   GPIO.cleanup()
   print('You pressed Ctrl+C!')
   sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

def go():
   pwm.start(100)
#   pwm.ChangeDutyCycle(100)
 
go() 

while True:
   time.sleep(1)
