import streamlit as st
from PIL import Image
from PIL.ImageFilter import *

st.markdown("<h1 style='text-align: center;'> Image Editor </h1>",unsafe_allow_html=True)
st.markdown("---")
image=st.file_uploader("Upload Image",type=["jpg","jpeg","png"])

size=st.empty()
mode=st.empty()
format_=st.empty()
if image:
    img=Image.open(image)
    st.markdown("<h2 style='text-align:center;'>Resizing</h2>",unsafe_allow_html=True)
    width=st.number_input("Width",value=img.width)
    height=st.number_input("Height",value=img.height)
    st.markdown("<h2 style='text-align:center;'>Rotation</h2>",unsafe_allow_html=True)
    degree=st.number_input("Degree")
    st.markdown("<h2 style='text-align:center;'>Filters</h2>",unsafe_allow_html=True)
    filters=st.selectbox("Filters",options=("None","Blur","Detail","Emboss","Smooth"))
    btn=st.button("Edit")
    if btn:
        edited=img.resize((width,height)).rotate(degree)
        filtered=edited
        if filtered!="None":
            if filter=="Blur":
                filtered=edited.filter(BLUR)
            elif filter=="Detail":
                filtered=edited.filter(DETAIL)
            elif filter=="Emboss":
                filtered=edited.filter(EMBOSS)
            else:
                filtered=edited.filter(SMOOTH)
        st.image(filtered)