import streamlit as st
from PIL import Image
import pytesseract
import easyocr
import os

# Initialize EasyOCR Reader (This can handle multiple languages too)
reader = easyocr.Reader(['en'])

# Set Tesseract path (adjust path depending on your installation)
# Make sure Tesseract is installed on your system (download from: https://github.com/tesseract-ocr/tesseract)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Adjust if needed

# Streamlit App Title
st.title("Smart OCR: Handwritten Text Recognition")

# File upload feature
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png", "pdf"])

# Processing the uploaded image
if uploaded_file is not None:
    # Load the image
    image = Image.open(uploaded_file)

    # Display the uploaded image
    st.image(image, caption="Uploaded Image", use_column_width=True)
    
    # Preprocess Image (Convert to grayscale if needed)
    st.write("Processing image...")

    # Extract text using Tesseract (Basic OCR)
    st.write("Extracting text using Tesseract OCR...")
    tesseract_text = pytesseract.image_to_string(image)

    # Extract text using EasyOCR (More advanced)
    st.write("Extracting text using EasyOCR...")
    easyocr_text = reader.readtext(uploaded_file)

    # Convert EasyOCR output to a string
    easyocr_text_output = "\n".join([item[1] for item in easyocr_text])

    # Display both outputs for comparison
    st.subheader("Text Extracted by Tesseract OCR:")
    st.text_area("Tesseract OCR Output", tesseract_text, height=200)

    st.subheader("Text Extracted by EasyOCR:")
    st.text_area("EasyOCR Output", easyocr_text_output, height=200)

    # Confidence score for EasyOCR (if applicable)
    easyocr_confidence = [item[2] for item in easyocr_text]
    if easyocr_confidence:
        st.subheader("EasyOCR Confidence Scores:")
        st.write("Confidence for each word:")
        st.write(easyocr_confidence)

    # Option to download the recognized text as a file
    st.subheader("Download Extracted Text")

    # Choose which text to export (Tesseract or EasyOCR)
    text_to_export = st.selectbox("Choose text to export", options=["Tesseract OCR", "EasyOCR"])

    # Export button for saving as a text file
    if text_to_export == "Tesseract OCR":
        text_output = tesseract_text
    elif text_to_export == "EasyOCR":
        text_output = easyocr_text_output

    if st.button("Download Text as .txt file"):
        # Save the text to a file
        output_file = "extracted_text.txt"
        with open(output_file, "w") as file:
            file.write(text_output)
        
        # Provide download link
        st.download_button(
            label="Download Text File",
            data=text_output,
            file_name=output_file,
            mime="text/plain"
        )