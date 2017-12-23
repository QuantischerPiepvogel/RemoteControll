import time, os
import RPi.GPIO as GPIO
import thread

GPIO.setmode(GPIO.BOARD)
GPIO.setup(33, GPIO.IN)

while GPIO.input(33) == GPIO.LOW:

  time.sleep(0.5)
  
os.system("sudo python RaspberryPI/MainControl.py")
