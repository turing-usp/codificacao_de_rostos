import streamlit as st
import DeepFace as dp
from PIL import Image
import pandas as pd
import os

datapath = "Turing_faces"
st.set_option('deprecation.showfileUploaderEncoding', False)

st.title("Quem é você no Turing? ")
uploaded_file = st.file_uploader("Mande uma foto sua...", type="jpg")


if uploaded_file is not None:
    path = "upload.jpg"
    image = Image.open(uploaded_file)
    user = image.save(path) 
    img = dp.detectFace(path)
    
    st.image(img, caption='Teu lindo rosto', use_column_width=True)
    dic = dp.make_dict(datapath)
    #df_new = dp.save_hash(path)             #Cria dataset somente com a nova imagem
    df =  pd.read_pickle("Turing_faces_hashed.plk")
    st.text("Procurando quem e voce...")
    ensemble, name = dp.compare_img_df(path,"uploaded.1" , dic, df)
    st.text(ensemble)

    st.text("Tu és " + str(name))



    # --------------------------------------
    os.chdir(datapath + chr(92) + name)
    for img in os.listdir('.'):
        st.image(img)
    
    os.chdir("..")
    os.chdir("..")




    os.remove(path)
