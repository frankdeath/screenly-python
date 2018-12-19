#!/usr/bin/env python
#
# https://raspberrypihq.com/use-a-push-button-with-raspberry-pi-gpio/
#

import RPi.GPIO as GPIO
import sapi

# Define pins
forward=24
backward=23
pause=26

# Ignore warnings
GPIO.setwarnings(False)
# Use the board numbering scheme for I/O pins
GPIO.setmode(GPIO.BOARD)
# Set pins 23, 24, and 26 as inputs with initial value to be pulled high (ON)
GPIO.setup(backward, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(forward, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(pause, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# Pin 25 is ground

# Callback functions for buttons
def backwardCallback(channel):
  print("Backward button was pushed!")
  sapi.prev()

def forwardCallback(channel):
  print("Forward button was pushed!")
  sapi.next()

def playPauseCallback(channel):
  print("Play/Pause button was pushed!")

# Register callback functions
GPIO.add_event_detect(backward, GPIO.FALLING,callback=backwardCallback)
GPIO.add_event_detect(forward, GPIO.FALLING,callback=backwardCallback)
GPIO.add_event_detect(pause, GPIO.FALLING,callback=playPauseCallback)

# pseudo main loop
message = input("Press enter to quit\n")

# Clean up
GPIO.cleanup()


