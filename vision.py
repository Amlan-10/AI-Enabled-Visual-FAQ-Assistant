import pytesseract
pytesseract.pytesseract.tesseract_cmd = "/usr/bin/tesseract"

from PIL import Image
import pytesseract

def extract_text_from_image(image):
    return pytesseract.image_to_string(image)
