import pytesseract
def read_image(im):
   return (pytesseract.image_to_string(im))
