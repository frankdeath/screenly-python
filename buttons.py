#!/usr/bin/env python
#
# https://raspberrypihq.com/use-a-push-button-with-raspberry-pi-gpio/
#

import RPi.GPIO as GPIO
import sapi
import signal
import time

# Allow the script to exit gracefully to insure cleanup is done
class GracefulExit:
  def __init__(self):
    self.timeToExit = False
    # Ctrl+C
    signal.signal(signal.SIGINT, self.exitNow)
    # kill
    signal.signal(signal.SIGTERM, self.exitNow)
    # systemd will send a hangup signal if the SIGTERM doesn't succeed
    signal.signal(signal.SIGHUP, self.exitNow)

  def exitNow(self, signum, frame):
    self.timeToExit = True

# Callback functions for buttons
def backwardCallback(channel):
  print("Backward button was pushed!")
  sapi.prev()

def forwardCallback(channel):
  print("Forward button was pushed!")
  sapi.next()

def playPauseCallback(channel):
  print("Play/Pause button was pushed!")
  sapi.pause()

def setupGPIO():
  # Define pins
  backward=37
  forward=38
  # Pin 39 is ground
  pause=40

  # Ignore warnings
  GPIO.setwarnings(False)

  # Use the board numbering scheme for I/O pins
  GPIO.setmode(GPIO.BOARD)

  # Set pins as inputs with initial value to be pulled high (ON)
  GPIO.setup(backward, GPIO.IN, pull_up_down=GPIO.PUD_UP)
  GPIO.setup(forward, GPIO.IN, pull_up_down=GPIO.PUD_UP)
  GPIO.setup(pause, GPIO.IN, pull_up_down=GPIO.PUD_UP)

  # Register callback functions
  GPIO.add_event_detect(backward, GPIO.FALLING,callback=backwardCallback)
  GPIO.add_event_detect(forward, GPIO.FALLING,callback=forwardCallback)
  GPIO.add_event_detect(pause, GPIO.FALLING,callback=playPauseCallback)

if __name__ == '__main__':
  print("Handling signals")
  ge = GracefulExit()

  print("Configuring GPIO")
  setupGPIO()

  print("Running main loop")
  while not ge.timeToExit:
    # Sleep for a relatively long time to minimize cpu usage, but still be responsive
    # sleeping for a hundredth of a second results in 1% cpu usage on a pi zero w
    time.sleep(1e-2)

  # Clean up
  print("Cleaning up!")
  GPIO.cleanup()
