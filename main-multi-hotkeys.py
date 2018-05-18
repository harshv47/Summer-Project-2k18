import snowboydecoder
#import sys
import signal
# Importing relay1.py to access relay functions defined therein
from relay1 import Relay

# Demo code for listening to two hotwords at the same time

interrupted = False


def signal_handler(signal, frame):
    global interrupted
    interrupted = True


def interrupt_callback():
    global interrupted
    return interrupted

# Remember models should always be a list
models = <address of different hotwords (meaning .pmdl files) in the pi>

# capture SIGINT signal, e.g., Ctrl+C
signal.signal(signal.SIGINT, signal_handler)

sensitivity = [0.5]*len(models)
detector = snowboydecoder.HotwordDetector(models, sensitivity=sensitivity)
"""
As an example:
Say you want to, on saying hotword1, flip a switch using relay
Write:
#If 23 is the pin where you connected the relay
relaypin= Relay(23)
callbacks = [lambda: relay1.set_on,
             lambda: relay1.set_off]
"""
callbacks = [lambda: <First callback>,
             lambda: <Second callback>]
print('Listening... Press Ctrl+C to exit')

# main loop
# make sure you have the same numbers of callbacks and models
detector.start(detected_callback=callbacks,
               interrupt_check=interrupt_callback,
               sleep_time=0.03)

detector.terminate()
