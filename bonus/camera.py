import streamlit as st
from PIL import Image


def convert_image(imagepath):
    # Create a pillow image instance
    image = Image.open(imagepath)

    # Convert the pillow image to grayscale
    gray_img = image.convert('L')

    # Render the grayscale image on the webpage
    st.image(gray_img)


st.subheader("Color to Grayscale Converter")

uploaded_image = st.file_uploader("Upload Image")

with st.expander("Start Camera"):
    # Start the camera
    camera_image = st.camera_input("Camera")

if camera_image:
    convert_image(camera_image)

if uploaded_image:
    convert_image(uploaded_image)
