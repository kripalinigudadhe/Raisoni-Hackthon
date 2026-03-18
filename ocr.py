import pytesseract
import easyocr
import cv2
import pytesseract

# Set the path for Tesseract OCR
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
# Linux/macOS users: Uncomment the following line and update the path
# pytesseract.pytesseract.tesseract_cmd = "/usr/bin/tesseract"

def recognize_text(image):
    # Use Tesseract OCR
    tesseract_text = pytesseract.image_to_string(image)
    
    # Use EasyOCR
    reader = easyocr.Reader(['en'])
    results = reader.readtext(image)
    easyocr_text = " ".join([res[1] for res in results])

    # Combine results
    combined_text = tesseract_text + "\n"
    # + easyocr_text

    return combined_text, None
