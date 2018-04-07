
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


@app.route('/getNextInstruction')
def nextInstruction():
    #0 = send an image
    #1 = send the temperature
    if CURRENT_INSTRUCTION== 0 or CURRENT_INSTRUCTION==1:
        return 0
    else :
        return -1

@app.route('/sendImageToServer',methods=['POST'])
def imageToServer():
    image = request.args.get('image')
    current_rasp_image = image
    #current_rasp_temp = request.args.get('temperature')

    if CURRENT_INSTRUCTION==0:
        describeImage(image)
    elif CURRENT_INSTRUCTION==1:
        readImage(image)
    else :
        pass

@app.route('/describeImage')
def describeImageRequest():
    CURRENT_INSTRUCTION = 0
    if current_rasp_image is None:
        pass
    else:
        describeImage(current_rasp_image)

@app.route('/readImage')
def readImageRequest():
    CURRENT_INSTRUCTION = 1
    if current_rasp_image is None:
        pass
    else:
        readImage(current_rasp_image)




#python aux functions
def describeImage(img):
    sentence = descriptor.describe(img)
    #send sentence to google
    CURRENT_INSTRUCTION = -1

def readImage(img):
    sentence = pytesseract.image_to_string(img)
    #send sentence to google
    CURRENT_INSTRUCTION= -1

if __name__ == '__main__':
    app.run(debug=True, port=8092, host='0.0.0.0')
