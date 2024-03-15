# Display Images

# import Image from pillow to open images
from PIL import Image
import streamlit as st

img = Image.open("image.webp")

# display image using streamlit
# width is used to set the width of an image
st.image(img, width=200)
