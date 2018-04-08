
#imported libraries
from flask import Flask
from clarifai.rest import Image as ClImage

from flask import request
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
@app.route('/')
def index():
    return "prova"


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
        pass
    else:
        sent = describeImage(current_rasp_image)
        #send to google
        return sent
    return  "ok"

@app.route('/readImage')
def readImageRequest():
    if current_rasp_image is None:
        pass
    else:
        sent = readImage(current_rasp_image)
        #send to google
        return sent
    return "ok"

@app.route('/getTemperature')
def getTemperatureRequest():
    if current_rasp_temp is None:
        pass
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
    app.run(debug=True, port=8092)
