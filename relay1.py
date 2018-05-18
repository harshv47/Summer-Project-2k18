import RPi.GPIO as GPIO
import time




#for a single channel Relay:

class Relay(object):
    def __init__(self, port):
        self.port = port
        # The script below using BCM GPIO 00..nn numbers
        GPIO.setmode(GPIO.BCM)

        # Set relay pins as output
        GPIO.setup(self.port, GPIO.OUT)

        self.on_state = GPIO.HIGH
        self.off_state = GPIO.LOW

    def set_on(self):
        GPIO.output(self.port, self.on_state)

    def set_off(self):
        GPIO.output(self.port, self.off_state)

        
