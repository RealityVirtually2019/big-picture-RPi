import RPi.GPIO as GPIO
import time
while True:
  GPIO.setmode(GPIO.BCM)
  GPIO.setwarnings(False)
  GPIO.setup(11,GPIO.OUT)
  print "LED on"
  GPIO.output(11,GPIO.HIGH)
  time.sleep(1)
  print "LED off"
  GPIO.output(11,GPIO.LOW)