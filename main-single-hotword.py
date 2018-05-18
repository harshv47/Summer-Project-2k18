import snowboydecoder
import sys
import signal

interrupted = False


def signal_handler(signal, frame):
    global interrupted
    interrupted = True


def interrupt_callback():
    global interrupted
    return interrupted


model = "/models/hey_bot.pmdl

# capture SIGINT signal, e.g., Ctrl+C
signal.signal(signal.SIGINT, signal_handler)

# you can play with sensitivity (should be something 0 to 1), I set(ed?) it to 1 because built the model with that
# setting it to a different value may make it not detect the sound
detector = snowboydecoder.HotwordDetector(model, sensitivity=1)
print('Listening... Press Ctrl+C to exit')

# main loop
detector.start(detected_callback=snowboydecoder.play_audio_file,
               interrupt_check=interrupt_callback,
               sleep_time=0.03)

detector.terminate()
