import cv2
import pyzbar.pyzbar as pyzbar
from PIL import Image
import streamlit as st

def parse_barcode(img):
    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect barcodes in the image
    barcodes = pyzbar.decode(gray)

    # Print the barcode data
    for barcode in barcodes:
        (x, y, w, h) = barcode.rect
        barcodeData = barcode.data.decode("utf-8")
        barcodeType = barcode.type
        text = f"{barcodeData} ({barcodeType})"
        st.write(text)

# Streamlit code
st.set_page_config(page_title="Barcode reader", page_icon=":barcode:", layout="wide")

# Capture image from camera
img_bytes = st.camera_input()

# Convert image bytes to PIL image
img = Image.open(img_bytes)
img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
parse_barcode(img)
