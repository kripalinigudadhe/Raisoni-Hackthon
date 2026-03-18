import streamlit as st
import numpy as np
from PIL import Image
from ocr import recognize_text
from export_utils import save_as_pdf, save_as_word
from preprocessing import preprocess_image

st.title("Smart OCR: Handwritten Text Recognition")

uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg", "pdf"])

if uploaded_file:
    image = Image.open(uploaded_file)
    img_array = np.array(image)

    # Preprocess the image
    processed_img = preprocess_image(img_array)

    # Display the uploaded image
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Recognize text
    recognized_text, confidence_scores = recognize_text(processed_img)

    st.subheader("Extracted Text")
    text_area = st.text_area("Editable Text", value=recognized_text, height=300)

    # Export options
    st.subheader("Export Options")
    col1, col2 = st.columns(2)

    with col1:
        save_as_pdf(text_area)  # PDF download button

    with col2:
        save_as_word(text_area)  # Word download button
