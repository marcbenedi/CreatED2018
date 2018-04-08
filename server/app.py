
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

    else:
        print('Unsupported action')
        result = "Action not found"
    return result



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

if __name__ == '__main__':
    #app.run(debug=True, port=8092)
    app.run(host='0.0.0.0', port=8080, ssl_context=context, debug=True)
