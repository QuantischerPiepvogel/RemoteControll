import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

GPIO.setup(18, GPIO.OUT) #Clock
GPIO.setup(16, GPIO.OUT) #Latch
GPIO.setup(12, GPIO.OUT) #Data
GPIO.setup(33, GPIO.IN)


def addRGB(r, g, b):
  shiftOne(b)
  time.sleep(0.01)
  shiftOne(g)
  time.sleep(0.01)
  shiftOne(r)
  time.sleep(0.01)

def refresh():
  GPIO.output(16, GPIO.HIGH)
  GPIO.output(16, GPIO.LOW)

def shiftOne(bool):
  GPIO.output(12, bool)
  GPIO.output(18, GPIO.HIGH)
  GPIO.output(18, GPIO.LOW)

while GPIO.input(33) == GPIO.LOW:
  shiftOne(1)
  refresh()
  time.sleep(1)
  
  for x in range(0, 23)
  
    shiftOne(0)
    refresh()
    time.sleep(1)

print("STOPPED")
