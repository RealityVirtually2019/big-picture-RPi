# importing the requests library 
from sense_hat import SenseHat
import requests 

sense = SenseHat()
  
# defining the api-endpoint  
API_ENDPOINT = "https://vsb5spplil.execute-api.us-east-1.amazonaws.com/update/trigger"
  
#data to be sent to api 
data = {"deviceId":"RPi-Three"} 

def trigger_event():
    # sending post request and saving response as response object
    r = requests.post(url = API_ENDPOINT, json = data)
    if r.ok:
        sense.show_message("RPi 3")
  
while True:
    for event in sense.stick.get_events():
        if event.direction == 'middle' and event.action == 'pressed':
            trigger_event()
        print(event.direction, event.action)

        
