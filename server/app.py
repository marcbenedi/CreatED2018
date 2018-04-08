
#imported libraries
from flask import Flask
from flask import request
from clarifai.rest import Image as ClImage
from OpenSSL import SSL

import pytesseract
import base64

#imported files
import descriptor
import temperature
app = Flask(__name__)

#tasks = send image, read image, send temperature, play music.
#           0           1               2           3
current_rasp_image = None
current_rasp_temp = None
current_rasp_humid = None
GOOGLE_ID ="1ab6abf0-442e-4a84-9d7b-5a9ebd2312ff"
# 0 = describe
# 1 = read_image
# 2 = temperature


@app.route('/', methods=['GET','POST'])
def hello_world():
    result = None
    request_json = request.get_json()
    action = request_json['result']['action']
    result = ""
    if action == 'describe.picture':
        print('Describe picture query')
        result = describeImageRequest()
    elif action == 'read.picture':
        print('Reading image')
        result = readImageRequest()

    elif action == 'get.temperature':
        print('Temperature')
        result = getTemperatureRequest()
    elif action == 'get.humidity':
        print ('Humidity')
        result = getHumidityRequest()
    else:
        print('Unsupported action')
        result = "Action not found"

    response =  createResponseMessage(result)

    return json.dumps(response), 201, {'Content-Type': 'application/json'}



@app.route('/putInfo',methods=['POST'])
def imageToServer():
    print (request.json)
#    image = request.args.get('image')
#    current_rasp_image = image
#    current_rasp_temp = request.args.get('temp')
    if request.headers['Content-Type'] == 'application/octet-stream':
        with open('./binary', 'wb') as f:
            f.write(request.data)
            f.close()
        current_rasp_image = ClImage(file_obj=open('binary', 'rb'))
        return "Binary message written!"
    elif request.headers['Content-Type'] == 'text/plain':
        print(request.data)
        return "Text Message: " + request.data



    return 200

@app.route('/describeImage')
def describeImageRequest():
    #Uncomment the following line to only test this method
    #current_rasp_image = ClImage(file_obj=open('binary', 'rb'))
    if current_rasp_image is None:
        return "Not getting image from camera"
    else:
        sent = describeImage(current_rasp_image)
        #send to google
        return sent
    return  "ok"

@app.route('/readImage')
def readImageRequest():
    if current_rasp_image is None:
        return "Not getting image from camera"
    else:
        sent = readImage(current_rasp_image)
        #send to google
        return sent
    return "ok"

@app.route('/getTemperature')
def getTemperatureRequest():
    if current_rasp_temp is None:
        return "Not getting temperature from sensor"
    else:
        sent = temperature.create_sentence(current_rasp_temp)
        #send to google
        return sent
    return "ok"

#python aux functions
def describeImage(img):
    sentence = descriptor.describe(img)
    return sentence

def readImage(img):
    sentence = pytesseract.image_to_string(img)
    return sentence

def getHumidityRequest():
    if current_rasp_humid is None:
        return "No available humidity data from the sensor"
    else:
        sent = "The current relative humidity is "+ str(current_rasp_humid)
        #send to google
        return sent
    return "ok"


def createResponseMessage (responseText):
    resp = {
    "speech": responseText,
    "displayText": responseText
    }
    return resp
if __name__ == '__main__':
    #app.run(debug=True, port=8092)
    app.run(host='0.0.0.0', port=8080, ssl_context=context, debug=True)
