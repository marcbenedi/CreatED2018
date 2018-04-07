
#imported libraries
from flask import Flask
import pytesseract
import sys
#imported files
sys.path.append('..')
import descriptor
app = Flask(__name__)

#tasks = send image, send temperature, play music.

CURRENT_INSTRUCTION = -1
# 0 = describe
# 1 = read_image
# 2 = temperature
@app.route('/')
def index():
    return "prova"


@app.route('/getNextInstruction')
def nextInstruction():
    if CURRENT_INSTRUCTION== 0 or CURRENT_INSTRUCTION==1:
        return 0


@app.route('/sendImageToServer',methods=['POST'])
def imageToServer(image):
    if CURRENT_INSTRUCTION==0:
        describeImage(image)
    elif CURRENT_INSTRUCTION==1:
        readImage(image)
    else :
        return "Unknown"

@app.route('/describeImage')
def describeImageRequest():
    CURRENT_INSTRUCTION = 0

@app.route('/readImage')
def readImageRequest():
    CURRENT_INSTRUCTION = 1




#python aux functions
def describeImage(img):
    sentence = descriptor.describe(img)
    #send sentence to google
    CURRENT_INSTRUCTION = -1
    
def readImage(img):
    sentence = pytesseract.image_to_string(img)
    #send sentence to google
    CURRENT_INSTRUCTION= -1
