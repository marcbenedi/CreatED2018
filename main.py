import raspberry_cam
import raspberry_tts
import image_reader

def read():
    im = raspberry_cam.get_image
    sentence = image_reader.read_image(im)
    raspberry_tts.say(sentence)

def describe():
    return "Not done yet!"
