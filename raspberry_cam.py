import picamera
import cv2

def get_image():
    camera = picamera.PiCamera()
    rawCapture = picamera.array.PiRGBArray(camera)

    camera.vflip = False
    camera.hflip = False
    camera.capture(rawCapture,format='bgr')
    img = rawCapture.array
    return img
