import subprocess
import shlex
from PIL import Image
import base64
import io
import os
def describeImage():
    moveBinaryFile()
    result = subprocess.check_output(shlex.split('th eval.lua -model trained_mod_cpu.t7 -image_folder imgs -num_images 2 -gpuid -1'))
    captions= []
    lines = result.split('\n')
    for l in lines:
        words = l.split()
        if len (words)>0:
            if words[0]=='image':
                captions.append(" ".join(words[2:]))
    print (captions)
    return captions[0]

def readimage(path):
    bytes = bytearray()
    count = os.stat(path).st_size / 2
    with open(path, "rb") as f:
        return bytearray(f.read())

def moveBinaryFile():
    bytes = readimage('binary')
    im = Image.open(io.BytesIO(bytes))
    im.save('imgs/img.jpg')
if __name__=="__main__":
    describeImage()
