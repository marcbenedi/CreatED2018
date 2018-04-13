import io
import time
from picamera import PiCamera
import requests

server_url = 'https://46.0.1.2'

def sendDataToServer():
    frame = get_image()
    temp = get_temperature()
    payload = {'image': frame, 'temp': temp}
    # headers = {'content_type': 'image/jpeg'}
    response = requests.post(url = server_url+'/putInfo', data = payload)

def get_image():
    camera = PiCamera()
    camera.capture('/home/pi/Desktop/image.jpg')
    return open('/home/pi/Desktop/image.jpg', 'rb')

def get_temperature():
    return 30


while True:
    sendDataToServer()
    time.sleep(5)
