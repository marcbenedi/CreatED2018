
#imported libraries
from flask import Flask
from flask import request
import pytesseract
import sys

sys.path.append('..')
#imported files
import descriptor
app = Flask(__name__)

#tasks = send image, read image, send temperature, play music.
#           0           1               2           3
current_rasp_image = None
current_rasp_temp = None
CURRENT_INSTRUCTION = -1
# 0 = describe
# 1 = read_image
# 2 = temperature
@app.route('/')
def index():
    return "prova"


@app.route('/putInfo',methods=['POST'])
def imageToServer():
    image = request.args.get('image')
    current_rasp_image = image
    current_rasp_temp = request.args.get('temp')

    if CURRENT_INSTRUCTION==0:
        describeImage(image)
    elif CURRENT_INSTRUCTION==1:
        readImage(image)
    else :
        pass
    return "ok"

@app.route('/describeImage')
def describeImageRequest():
    CURRENT_INSTRUCTION = 0
    if current_rasp_image is None:
        pass
    else:
        sent = describeImage(current_rasp_image)
        #send to google
    return "ok"

@app.route('/readImage')
def readImageRequest():
    CURRENT_INSTRUCTION = 1
    if current_rasp_image is None:
        pass
    else:
        sent = readImage(current_rasp_image)
        #send to google
    return "ok"



#python aux functions
def describeImage(img):
    sentence = descriptor.describe(img)
    return sentence

def readImage(img):
    sentence = pytesseract.image_to_string(img)
    return sentence

if __name__ == '__main__':
    app.run(debug=True, port=65010)
