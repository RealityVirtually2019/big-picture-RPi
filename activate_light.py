import RPi.GPIO as GPIO
import time
import http.client

while True:
  conn = http.client.HTTPSConnection('https://vsb5spplil.execute-api.us-east-1.amazonaws.com/prod/status?device_id=light1', 443)
  conn.request('GET', '/') # <---
  r = conn.getresponse()
  print(r.read())
  GPIO.setmode(GPIO.BCM)
  GPIO.setwarnings(False)
  GPIO.setup(11,GPIO.OUT)
  print "LED on"
  GPIO.output(11,GPIO.HIGH)
  time.sleep(1)
  print "LED off"
  GPIO.output(11,GPIO.LOW)